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

    def __init__(self, message, func_name, start_lineno, end_lineno=None):
        self.message = message
        self.func_name = func_name
        self.start_lineno = start_lineno
        self.end_lineno = end_lineno if end_lineno else start_lineno

    def __lt__(self, other):
        if self.start_lineno == other.start_lineno:
            return self.end_lineno < other.end_lineno
        return self.start_lineno < other.start_lineno

    def __str__(self):
        if self.end_lineno == self.start_lineno:
            return 'line {} ({}) : {}'.format(
                self.start_lineno, self.func_name, self.message)
        return 'line {}-{} ({}) : {}'.format(
            self.start_lineno, self.end_lineno, self.func_name, self.message)


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

        # Caches data about func_block.
        self.sorted_blocks = self.func.get_sorted_blocks()
        self.linenos = self._get_linenos_in_func()
        self.variables = self._get_variables_in_func()

        # Global caches.
        self._SLICE_CACHE = {}

    # Gets the line numbers in a function.
    def _get_linenos_in_func(self):
        return sorted([lineno for block in self.sorted_blocks
                              for lineno in block.get_instruction_linenos()])

    # Gets the variables in a function.
    def _get_variables_in_func(self):
        variables = set()
        for block in self.sorted_blocks:
            for instr in block.get_instructions():
                for var in instr.defined:
                    variables.add(var)
        return variables

    # -------------------------------------
    # ---------- GENERATES SLICE ----------
    # -------------------------------------

    # Gets set of line numbers in a slice.
    def _get_instructions_in_slice(self, start_lineno, **kwargs):
        visited = set()
        queue = [start_lineno]
        min_lineno = start_lineno

        # Parse keyword arguments.
        include_control = kwargs['include_control'] if 'include_control' in kwargs else True
        exclude_vars = kwargs['exclude_vars'] if 'exclude_vars' in kwargs else {}

        while queue:
            # Get instruction.
            cur_lineno = queue.pop()
            instr = self.info.get_instruction(cur_lineno)

            # If instruction is a valid instruction.
            if instr and cur_lineno not in visited:
                # Get instruction info and add to slice.
                instr_info = self.info.get_instruction_info(cur_lineno)

                # Trace line numbers of referenced variables.
                for var in instr.referenced:
                    # Exclude function names, variables only referenced,
                    # and variables in exclude_vars.
                    if var in instr_info.in_node and var not in exclude_vars:
                        for block_label, lineno in instr_info.in_node[var]:
                            queue.append(lineno)
                            min_lineno = min(lineno, min_lineno)

                # Add line wraps.
                for lineno in instr.multiline:
                    queue.append(lineno)
                    min_lineno = min(lineno, min_lineno)

                # Trace line numbers of control variables if include_control is True
                # or a line before control is referenced.
                if (instr.control and (instr.control not in visited) and
                    (include_control or instr.control > min_lineno)):
                    queue.append(instr.control)

            # Mark current instruction as visited.
            visited.add(cur_lineno)

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

    # ----------------------------------------
    # ---------- CONDENSES CFG ---------------
    # ----------------------------------------

    # Condenses successors into one block if they are equal.
    def _condense_cfg_fold_redundant_branch(self, block):
        successors = list(block.successors.values())

        if len(successors) > 1 and block.check_successor_equality():
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

    # ------------------------------------------------------------------
    # ---------- GENERATES CONDENSED SLICE AND SLICE MAP ---------------
    # ------------------------------------------------------------------

    # Gets a slice for the function block for the given line number.
    def _get_slice(self, instrs):
        slice_func = self._generate_cfg_slice(instrs)
        slice_func = self.condense_cfg(slice_func)
        return slice_func

    # Gets a slice for the function block from the cache.
    def get_slice(self, instrs):
        instrs = frozenset(instrs)
        if instrs not in self._SLICE_CACHE:
            slice_cfg = self._get_slice(instrs)
            slice_complexity = slice_cfg.get_cyclomatic_complexity()
            self._SLICE_CACHE[instrs] = {'complexity': slice_complexity,
                                         'cfg': slice_cfg}
        return self._SLICE_CACHE[instrs]

    # Gets map of line number to slice.
    # Parameter kwargs is arguments to _get_instructions_in_slice().
    def get_slice_map(self, **kwargs):
        slice_map = {}
        for lineno in self.linenos:
            instrs = self._get_instructions_in_slice(lineno, **kwargs)
            if instrs:
                slice_map[lineno] = self.get_slice(instrs)
        return slice_map

    # ----------------------------------------------
    # ---------- COMPARES SLICE MAPS ---------------
    # ----------------------------------------------

    # Groups line numbers with greater than max diff between slices.
    def _group_linenos(self, linenos, max_diff_linenos):
        generate_group = lambda linenos, max_diff: (
            split(linenos, where(diff(linenos) >= max_diff)[0] + 1))

        # Group line numbers.
        linenos = sorted(linenos)
        groups = generate_group(linenos, max_diff_linenos)

        # Determine if comments/blank lines connect groups.
        if len(groups) > 1:
            unimportant_in_func = self.func.blank_lines.union(self.func.comments)
            for leftgroup, rightgroup in zip(groups[:-1], groups[1:]):
                minval = max(leftgroup) + 1
                maxval = min(rightgroup)
                range_linenos = set(range(minval, maxval))

                # Add linenos with comments/blank lines.
                unimportant = range_linenos.intersection(unimportant_in_func)
                if len(unimportant) == len(range_linenos):
                    linenos.extend(list(range_linenos))

            # Regenerate groups of line numbers.
            linenos = sorted(linenos)
            groups = generate_group(linenos, max_diff_linenos)
        return groups

    # Adjust line numbers based on multiline groups.
    def _adjust_linenos_multiline_groups(self, linenos, slice_map):
        final_linenos = set()
        for lineno in linenos:
            instr = self.info.get_instruction(lineno)
            valid_lines = [group_lineno not in slice_map or group_lineno in linenos
                           for group_lineno in instr.multiline]
            if all(valid_lines):
                final_linenos.add(lineno)
                final_linenos |= instr.multiline
        return final_linenos

    # Gets groups of line numbers with greater than max diff between slices.
    def _compare_slice_maps(self, slice_map, reduced_slice_map,
                            min_diff_complexity, max_diff_linenos):
        linenos = set()

        # Get line numbers with reduced complexity.
        for lineno in self.linenos:
            if lineno in slice_map and lineno in reduced_slice_map:
                slice_complexity = slice_map[lineno]['complexity']
                reduced_slice_complexity = reduced_slice_map[lineno]['complexity']

                # If enough decrease in complexity, add line and grouped lines.
                if (slice_complexity - reduced_slice_complexity) >= min_diff_complexity:
                    linenos.add(lineno)

        # Groups line numbers within the epsilon of each other.
        linenos = self._adjust_linenos_multiline_groups(linenos, slice_map)
        return self._group_linenos(linenos, max_diff_linenos)

    # ----------------------------------------------
    # ---------- GENERATES SUGGESTIONS ---------------
    # ----------------------------------------------

    # Generates suggestions from a map of range of lineno to list of variables.
    def _generate_suggestions_variable_map(self, lineno_variables_map):
        suggestions = []
        for key, variables in lineno_variables_map.items():
            # Generate message for suggestion.
            message = 'Try creating a new function with parameter'
            if len(variables) == 1:
                message += ' {}'.format(variables[0])
            else:
                message += 's {}'.format(', '.join(variables))

            # Add suggestion.
            min_lineno, max_lineno = key
            suggestions.append(Suggestion(message, self.func.label, min_lineno, max_lineno))
        return suggestions

    # Gets the suggestions on a slice based on removing variables.
    def _get_suggestions_remove_variables(self, slice_map, debug=False):
        suggestions_map = {}

        # Gets map of linenos to variables to generate suggestions.
        for var in self.variables:
            reduced_slice_map = self.get_slice_map(exclude_vars=[var])
            linenos = self._compare_slice_maps(slice_map, reduced_slice_map,
                                               Slice.MIN_DIFF_COMPLEXITY,
                                               Slice.MAX_DIFF_FOR_GROUPING)

            # Iterates through groups of linenos.
            for group in linenos:
                if len(group) >= Slice.MIN_LINES_FOR_SUGGESTION:
                    key = (min(group), max(group))
                    if key not in suggestions_map:
                        suggestions_map[key] = []
                    suggestions_map[key].append(var)

        # Returns list of suggestions from suggestions map.
        return self._generate_suggestions_variable_map(suggestions_map)

    # Gets the suggestions on how to improve the function.
    def get_suggestions(self, debug=False):
        suggestions = []
        slice_map = self.get_slice_map()

        suggestions.extend(self._get_suggestions_remove_variables(slice_map, debug))

        return sorted(suggestions)

    # Gets the complexity for each line multiplied by line number.
    def get_lineno_complexity(self, debug=True):
        slice_map = self.get_slice_map()
        lineno_complexity = 0
        for idx, lineno in enumerate(sorted(slice_map.keys())):
            reduced_slice_complexity = slice_map[lineno]['complexity']
            lineno_complexity += (reduced_slice_complexity * idx)
        lineno_complexity = float(lineno_complexity) / (idx + 1)
        return lineno_complexity
