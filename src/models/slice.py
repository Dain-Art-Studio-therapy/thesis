# File name: slice.py
# Author: Nupur Garg
# Date created: 2/20/2017
# Python Version: 3.5


from numpy import array, diff, where, split
import copy

from src.models.block import FunctionBlock, Block, BlockList
from src.models.blockinfo import FunctionBlockInformation, ReachingDefinitions
from src.models.dataflowanalysis import ReachingDefinitionsAnalysis


class Suggestion(object):
    """
    Represents a suggestion to be made to the user.
    """

    def __init__(self, message, start_lineno, end_lineno=None):
        self.message = message
        self.start_lineno = start_lineno
        self.end_lineno = end_lineno if end_lineno else start_lineno

    def __lt__(self, other):
        if self.start_lineno == other.start_lineno:
            return self.end_lineno < other.end_lineno
        return self.start_lineno < other.start_lineno

    def __str__(self):
        if self.end_lineno == self.start_lineno:
            return '{} : {}'.format(self.start_lineno, self.message)
        return '{}-{} : {}'.format(self.start_lineno, self.end_lineno, self.message)


class Slice(object):
    """
    Generates a slice for a function block.

    func: obj
        FunctionBlock for the current function.
    info: obj
        FunctionBlockInformation containg ReachingDefinitions for current block.
    """

    MIN_DIFF_COMPLEXITY = 3
    MAX_DIFF_FOR_GROUPING = 2
    MIN_LINES_FOR_SUGGESTION = 3

    def __init__(self, func):
        self.func = func
        analysismethod = ReachingDefinitionsAnalysis()
        self.info = analysismethod.analyze(self.func)
        self.sorted_blocks = self.func.get_sorted_blocks()
        self._SLICE_CACHE = {}

    # Gets the variables in a slice.
    def _get_variables_in_slice(self):
        variables = set()
        for block in self.sorted_blocks:
            for instr in block.get_instructions():
                for var in instr.defined:
                    variables.add(var)
        return variables

    # Gets set of line numbers in a slice.
    def _get_instructions_in_slice(self, start_lineno, **kwargs):
        visited = set([start_lineno])
        queue = [start_lineno]
        min_lineno = start_lineno

        # Parse keyword arguments.
        include_control = (kwargs['include_control']
                          if 'include_control' in kwargs else True)
        remove_vars = kwargs['remove_vars'] if 'remove_vars' in kwargs else None

        while queue:
            # Get instruction and instruction info at line number.
            lineno = queue.pop()
            instr = self.info.get_instruction(lineno)
            instr_info = self.info.get_instruction_info(lineno)

            # Adds instruction (as line number) to slice.
            visited.add(lineno)

            # Trace line numbers of referenced variables.
            for var in instr.referenced:
                # Exclude function names and other variables never set.
                if var in instr_info.in_node:
                    for block_label, lineno in instr_info.in_node[var]:
                        if lineno not in visited:
                            queue.append(lineno)
                            min_lineno = min(lineno, min_lineno)

            # Trace line numbers of control variables if include_control is True
            # or a line before control is referenced.
            if (instr.control and (instr.control not in visited) and
                (include_control or instr.control > min_lineno)):
                queue.append(instr.control)

        # Returns set of line numbers instructions.
        return visited

    # Creates a FunctionBlock representing a CFG from a
    # set of instructions in sorted blocks.
    def _generate_cfg_slice(self, slice_instrs):
        block_map = {} # function block number : slice block number
        slice_func = FunctionBlock(self.func.label)

        for block in self.sorted_blocks:
            # Get all instructions in this block that are in the slice.
            linenos = block.get_instruction_linenos().intersection(slice_instrs)

            # Create a copy of the block.
            if not block_map:
                curr_bloc = slice_func
            else:
                curr_bloc = Block()
            block_map[block.label] = curr_bloc

            # Copy instructions in the block to block copy.
            for lineno in linenos:
                instruction = block.get_instruction(lineno)
                curr_bloc.add_instruction(instruction)

            # Copy the block's successors.
            for successor in block.successors:
                if successor in block_map:
                    curr_bloc.add_successor(block_map[successor])

            # Copy the block's predecessors.
            for predecessor in block.predecessors:
                if predecessor in block_map:
                    curr_bloc.add_predecessor(block_map[predecessor])

        return slice_func

    # Condenses successors into one block if they are equal.
    def _condense_cfg_fold_redundant_branch(self, block):
        successors = list(block.successors.values())

        if len(successors) > 1 and successors[1:] == successors[:-1]:
            for successor in successors[1:]:
                successor.destroy()

    # Removes empty block if block is empty and isn't a function block.
    def _condense_cfg_remove_empty_block(self, block, func):
        successor = block.get_first_successor()

        # If block is empty and isn't a function block, remove block.
        if (len(block.successors) == 1 and block != func and
            len(block.get_instruction_linenos()) == 0):
            # Remove predecessors.
            while block.predecessors:
                predecessor = block.get_first_predecessor()
                predecessor.replace_successor(block, successor)

            # Remove successor.
            successor.remove_predecessor(block)
            block.set_successors([])

    # Combines block if single successor has one predecessor.
    def _condense_cfg_combine_blocks(self, block):
        successor = block.get_first_successor()

        # If successor has one predecessor, merge blocks.
        if len(block.successors) == 1 and len(successor.predecessors) == 1:
            # Add instructions to current block.
            for instruction in successor.get_instructions():
                block.add_instruction(instruction)

            # Change block's successors and successor's predecessors.
            block.remove_successor(successor)
            while successor.successors:
                new_successor = successor.get_first_successor()
                new_successor.replace_predecessor(successor, block)

    # Skips successors if successor is empty and leads to a branch.
    def _condense_cfg_hoist_branch(self, block):
        successor = block.get_first_successor()

        # If successor is empty and ends in a branch, skip successor.
        if (len(block.successors) == 1 and len(successor.successors) > 1 and
            len(successor.get_instruction_linenos()) == 0):
            successors = successor.successors.values()
            block.set_successors(successors)

    # Runs through one pass of condensing a FunctionBlock representing a CFG.
    def _condense_cfg_helper(self, func):
        visited = set()
        queue = [func]

        while queue:
            block = queue.pop()
            visited.add(block.label)

            # Run optimization functions on the block.
            self._condense_cfg_fold_redundant_branch(block)
            self._condense_cfg_remove_empty_block(block, func)
            self._condense_cfg_combine_blocks(block)
            self._condense_cfg_hoist_branch(block)

            # Add successors to queue if not visited.
            for label, successor in block.successors.items():
                if label not in visited:
                    queue.append(successor)
        return func

    # Condenses a FunctionBlock representing a CFG.
    def condense_cfg(self, func):
        func = copy.deepcopy(func)
        func_copy = None
        while func != func_copy:
            func_copy = copy.deepcopy(func)
            func = self._condense_cfg_helper(func)
        return func

    # Gets a slice for the function block for the given line number.
    def get_slice(self, instrs):
        slice_func = self._generate_cfg_slice(instrs)
        slice_func = self.condense_cfg(slice_func)
        return slice_func


    #### SECTION: NEED TO FINISH (AND TEST)


    # Gets map of line number to slice.
    # Parameter kwargs is arguments to _get_instructions_in_slice().
    def get_slice_map(self, **kwargs):
        slice_map = {}
        for block in self.sorted_blocks:
            for lineno in block.get_instruction_linenos():
                instrs = frozenset(self._get_instructions_in_slice(lineno, **kwargs))
                if instrs:
                    # Use cache of slices of instructions to CFGs.
                    if instrs not in self._SLICE_CACHE:
                        slice_cfg = self.get_slice(instrs)
                        slice_complexity = slice_cfg.get_cyclomatic_complexity()
                        self._SLICE_CACHE[instrs] = {'complexity': slice_complexity,
                                                     'cfg': slice_cfg}
                    slice_map[lineno] = self._SLICE_CACHE[instrs]
        return slice_map

    # Gets groups of line numbers with greater than max diff between slices.
    def _compare_slice_maps(self, slice_map, reduced_slice_map,
                            min_diff_complexity, max_diff_linenos):
        linenos = []
        for lineno in sorted(slice_map.keys()):
            if lineno in slice_map and lineno in reduced_slice_map:
                slice_complexity = slice_map[lineno]['complexity']
                reduced_slice_complexity = reduced_slice_map[lineno]['complexity']
                if (slice_complexity - reduced_slice_complexity) >= min_diff_complexity:
                    linenos.append(lineno)

        # Groups line numbers within the epsilon of each other.
        linenos = sorted(linenos)
        return split(linenos, where(diff(linenos) >= max_diff_linenos)[0] + 1)

    # Gets the suggestions on a slice based on removing control.
    def _get_suggestions_remove_control(self, slice_map, debug):
        suggestions = []

        # Get line numbers with decrease in complexity from control.
        reduced_slice_map = self.get_slice_map(include_control=False)
        linenos = self._compare_slice_maps(slice_map, reduced_slice_map,
                                           Slice.MIN_DIFF_COMPLEXITY,
                                           Slice.MAX_DIFF_FOR_GROUPING)

        # Generate suggestions for the groups of line numbers.
        for group in linenos:
            if len(group) >= Slice.MIN_LINES_FOR_SUGGESTION:
                message = "Control is complex. Try creating a new function."
                suggestions.append(Suggestion(message, min(group), max(group)))
        return suggestions

    # Gets the suggestions on a slice based on removing variables.
    def _get_suggestions_remove_variables(self, slice_map, debug=False):
        suggestions = []
        variables = self._get_variables_in_slice()
        for var in variables:
            reduced_slice_map = self.get_slice_map(remove_vars=[var])
            linenos = self._compare_slice_maps(slice_map, reduced_slice_map,
                                               Slice.MIN_DIFF_COMPLEXITY,
                                               Slice.MAX_DIFF_FOR_GROUPING)

            # Generate suggestions for the groups of line numbers.
            for group in linenos:
                if len(group) >= Slice.MIN_LINES_FOR_SUGGESTION:
                    message = "Try creating a new function with parameter {}".format(var)
                    suggestions.append(Suggestion(message, min(group), max(group)))
        return suggestions

    # Gets the suggestions on how to improve the function.
    def get_suggestions(self, debug=False):
        suggestions = []
        slice_map = self.get_slice_map()

        suggestions.extend(self._get_suggestions_remove_control(slice_map, debug))
        suggestions.extend(self._get_suggestions_remove_variables(slice_map, debug))

        if suggestions:
            for suggestion in suggestions:
                print(suggestion)
        return suggestions
