# File name: slice.py
# Author: Nupur Garg
# Date created: 2/20/2017
# Python Version: 3.5


from src.globals import *
from numpy import array, diff, where, split
from enum import Enum
import copy

from src.models.block import FunctionBlock, Block, BlockList
from src.models.blockinfo import FunctionBlockInformation, ReachingDefinitions
from src.models.dataflowanalysis import *
from src.models.structures import Queue


class SuggestionType(Enum):
    __order__ = 'REMOVE_VAR, SIMILAR_REF, DIFF_REF_LIVAR'
    REMOVE_VAR = 1
    SIMILAR_REF = 2
    DIFF_REF_LIVAR = 3



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
    MAX_VARIABLES_PARAMETER = 6
    MIN_LINES_FOR_SUGGESTION = 3
    MIN_LINES_FUNC_NOT_IN_SUGGESTION = 5
    MAX_DIFF_REF_LIVE_VAR = 4

    def __init__(self, func):
        self.func = func
        self.func = self.condense_cfg(self.func)
        analysismethod = ReachingDefinitionsAnalysis()
        self.reaching_def_info = analysismethod.analyze(self.func)

        analysismethod = LiveVariableAnalysis()
        self.live_var_info = analysismethod.analyze(self.func)

        # Caches data about func_block.
        self.sorted_blocks = self.func.get_sorted_blocks()
        self.linenos = self.func.get_linenos_in_func()
        self.variables = self._get_variables_in_func()

        # Global caches.
        self._SLICE_CACHE = {}

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
        queue = Queue()
        queue.enqueue(start_lineno)

        # Parse keyword arguments.
        include_control = kwargs.get('include_control', True)
        exclude_vars = kwargs.get('exclude_vars', {})

        while not queue.empty():
            # Get instruction.
            cur_lineno = queue.dequeue()
            instr = self.reaching_def_info.get_instruction(cur_lineno)

            # Process instruction if it has not been visited.
            if instr and cur_lineno not in visited:
                instr_info = self.reaching_def_info.get_instruction_info(cur_lineno)

                # Trace line numbers of referenced variables except:
                #   - Variables only referenced in func (e.g. function names).
                #   - Variables in exclude_vars.
                for var in instr.referenced:
                    if var in instr_info.in_node and var not in exclude_vars:
                        for _, lineno in instr_info.in_node[var]:
                            queue.enqueue(lineno)

                # Add line wraps.
                for lineno in instr.multiline:
                    queue.enqueue(lineno)

                # Add control if include_control or a line before control is referenced.
                if instr.control and (include_control or instr.control > queue.min()):
                    queue.enqueue(instr.control)

            # Mark current instruction as visited.
            visited.add(cur_lineno)

        # Returns set of line numbers instructions.
        return visited

    # Creates a FunctionBlock representing a CFG from a set of instruction linenos.
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

    # TODO: REVIEW!!!
    # Adjust line numbers based on multiline groups.
    def _adjust_linenos_multiline_groups(self, linenos, unimportant_linenos):
        final_linenos = set()
        for cur_lineno in linenos:
            instr = self.reaching_def_info.get_instruction(cur_lineno)
            valid_lines = [lineno in unimportant_linenos or lineno in linenos
                           for lineno in instr.multiline]
            if all(valid_lines):
                final_linenos.add(cur_lineno)
                final_linenos |= instr.multiline
        return final_linenos

    # Groups line numbers with greater than max diff between slices.
    def _generate_groups(self, linenos, max_diff_linenos):
        linenos = sorted(linenos)
        return split(linenos, where(diff(linenos) >= max_diff_linenos)[0] + 1)

    # Groups line numbers with greater than max diff between slices.
    # Adds comments/blank lines to connect groups.
    def _group_linenos(self, linenos, max_diff_linenos, unimportant_linenos):
        groups = self._generate_groups(linenos, max_diff_linenos)

        # Connects groups separated by comments/blank lines.
        if len(groups) > 1:
            for leftgroup, rightgroup in zip(groups[:-1], groups[1:]):
                linenos_in_gap = set(range(max(leftgroup)+1, min(rightgroup)))

                # Add linenos if all linenos in gap are comments/blank lines.
                unimportant = linenos_in_gap.intersection(unimportant_linenos)
                if len(unimportant) == len(linenos_in_gap):
                    linenos |= linenos_in_gap

            groups = self._generate_groups(linenos, max_diff_linenos)
        return groups

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
        unimportant_linenos = self.func.blank_lines.union(self.func.comments)
        linenos = self._adjust_linenos_multiline_groups(linenos, unimportant_linenos)
        return self._group_linenos(linenos, max_diff_linenos, unimportant_linenos)

    # -----------------------------------------------------
    # ---------- GENERATES SUGGESTION TYPES ---------------
    # -----------------------------------------------------

    # Gets suggestions based on removing variables.
    def _get_suggestions_remove_variables(self, slice_map, debug=False):
        suggestions = set()

        # Gets map of linenos to variables to generate suggestions.
        for var in self.variables:
            reduced_slice_map = self.get_slice_map(exclude_vars=[var])
            linenos = self._compare_slice_maps(slice_map, reduced_slice_map,
                                               Slice.MIN_DIFF_COMPLEXITY,
                                               Slice.MAX_DIFF_FOR_GROUPING)

            # Adds groups of linenos.
            for group in linenos:
                if len(group) >= Slice.MIN_LINES_FOR_SUGGESTION:
                    suggestions.add((min(group), max(group)))
        return suggestions, SuggestionType.REMOVE_VAR

    # Gets suggestions based on similar references in a block.
    def _get_suggestions_similar_ref_block(self, debug=False):
        suggestions = set()

        for block in self.sorted_blocks:
            prev_ref_set = set()
            min_lineno = None
            max_lineno = None

            # Finds similar references in consequtive lines within a block.
            for instr in block.get_instructions():
                if not instr.referenced or instr.referenced != prev_ref_set:
                    if len(instr.referenced) > 1:
                        if (min_lineno and (self._range(min_lineno, max_lineno) >=
                                            Slice.MIN_LINES_FOR_SUGGESTION)):
                            suggestions.add((min_lineno, max_lineno))
                    min_lineno = instr.lineno
                max_lineno = instr.lineno
                prev_ref_set = instr.referenced
        return suggestions, SuggestionType.SIMILAR_REF

    # Gets suggestions based on differences in live var and referenced in a block.
    def _get_suggestions_diff_reference_livevar_block(self, debug=False):
        suggestions = set()
        linenos = set()
        multiline = set()
        cur_control = set()
        exclude_control = set()

        for block in reversed(self.sorted_blocks):
            info = self.live_var_info.get_block_info(block)
            instrs = set()

            # Get properities of the block.
            for instr in block.get_instructions():
                cur_control.add(instr.control)
                multiline |= instr.multiline
                instrs.add(instr.lineno)

            # Only continue building suggestion if any instrs depending on
            # current block's instrs are included in linenos variable.
            if ((len(info.in_node) - len(info.referenced)) > Slice.MAX_DIFF_REF_LIVE_VAR
                and not instrs.intersection(exclude_control)):
                linenos |= instrs
            else:
                intersection = multiline.intersection(linenos)
                # Only add if all lines in the multiline group are in linenos.
                if (len(linenos) >= Slice.MIN_LINES_FOR_SUGGESTION and
                    (len(intersection) == len(multiline) or not intersection)):
                    suggestions.add((min(linenos), max(linenos)))
                exclude_control |= cur_control

                linenos = set()
                multiline = set()
                cur_control = set()
        return suggestions, SuggestionType.DIFF_REF_LIVAR

    # ------------------------------------------------
    # ---------- GENERATES SUGGESTIONS ---------------
    # ------------------------------------------------

    # Gets the length of the range of the line numbers.
    def _range(self, min_lineno, max_lineno):
        return max_lineno - min_lineno + 1

    # Determines if the suggestion is valid.
    def _is_valid_suggestion(self, variables, min_lineno, max_lineno):
        variables = set(variables)
        lines_suggestions = self._range(min_lineno, max_lineno)
        lines_func = len(self.linenos) - lines_suggestions

        return (len(variables) <= Slice.MAX_VARIABLES_PARAMETER and
                lines_suggestions >= Slice.MIN_LINES_FOR_SUGGESTION and
                lines_func >= Slice.MIN_LINES_FUNC_NOT_IN_SUGGESTION and
                variables != self.func.get_function_parameters())

    # Gets the variables referenced in range of line numbers.
    def _get_referenced_variables(self, min_lineno, max_lineno):
        variables = set()
        defined = set()
        for lineno in range(min_lineno, max_lineno+1):
            instr_info = self.live_var_info.get_instruction_info(lineno)
            if instr_info:
                for var in instr_info.referenced:
                    if var not in defined:
                        variables.add(var)
                for var in instr_info.defined:
                    defined.add(var)
        return sorted(list(variables))

    # Creates the message for a suggestion.
    def _get_suggestion_message(self, variables, types):
        message = ''

        # Add suggestion types to message.
        message += '('
        message += ', '.join([suggestion_type.name.lower()
                             for suggestion_type in types])
        message += ')'

        # Add parameters to message.
        message += ' Try creating a new function with parameter'
        if len(variables) == 1:
            message += ' {}'.format(variables[0])
        else:
            message += 's {}'.format(', '.join(variables))
        return message

    # Generates suggestions from a map of range of lineno to list of variables.
    def _generate_suggestions(self, suggestion_map):
        suggestions = []
        for key, types in suggestion_map.items():
            min_lineno, max_lineno = key
            variables = self._get_referenced_variables(min_lineno, max_lineno)

            # Generate message if the number of vars within max vars in func.
            if self._is_valid_suggestion(variables, min_lineno, max_lineno):
                message = self._get_suggestion_message(variables, types)
                suggestions.append(Suggestion(message, self.func.label,
                                              min_lineno, max_lineno))
        return suggestions

    # Adds suggestions to suggestion map.
    def _add_suggestion_map(self, suggestion_map, suggestions, suggestion_type):
        for suggestion in suggestions:
            if suggestion not in suggestion_map:
                suggestion_map[suggestion] = set()
            suggestion_map[suggestion].add(suggestion_type)

    # Adds suggestions of function type to suggestion map.
    def _add_suggestions(self, suggestion_map, func, **kwargs):
        suggestions, suggestion_type = func(**kwargs)
        self._add_suggestion_map(suggestion_map, suggestions, suggestion_type)

    # TODO: Each function should return suggestions, hint.
    # TODO: Compile the suggestions in this function.
    # Gets the suggestions on how to improve the function.
    def get_suggestions(self, debug=False):
        suggestion_map = {}
        slice_map = self.get_slice_map()

        # Get the suggestions through various methods.
        self._add_suggestions(suggestion_map,
                              func=self._get_suggestions_remove_variables,
                              slice_map=slice_map, debug=debug)
        self._add_suggestions(suggestion_map,
                              func=self._get_suggestions_similar_ref_block,
                              debug=debug)
        self._add_suggestions(suggestion_map,
                              func=self._get_suggestions_diff_reference_livevar_block,
                              debug=debug)

        # Generate list of final suggestions.
        final_suggestions = self._generate_suggestions(suggestion_map)
        return sorted(final_suggestions)

    # TODO: REMOVE.
    def print_live_var_data(self):
        self.func = self.condense_cfg(self.func)
        analysismethod = LiveVariableAnalysis()
        self.live_var_info = analysismethod.analyze(self.func)

        print("")
        print("--------------------------")
        print("------{}-----".format(self.func.label))
        print("--------------------------")
        print(self.func)
        for func, info in self.live_var_info.blocks():
            print(func.label)
            print("\tREF {}".format(sorted(list(info.referenced))))
            print("\tDEF {}".format(sorted(list(info.defined))))
            print("\tIN  {}".format(sorted(list(info.in_node))))
            print("\tOUT {}".format(sorted(list(info.out_node))))
            print("")
        print("")
        print("")

    # TODO: REMOVE (or refactor).
    # Gets the complexity for each line multiplied by line number.
    def get_lineno_complexity(self, debug=True):
        slice_map = self.get_slice_map()
        lineno_complexity = 0
        for idx, lineno in enumerate(sorted(slice_map.keys())):
            reduced_slice_complexity = slice_map[lineno]['complexity']
            lineno_complexity += (reduced_slice_complexity * idx)
        length = len(slice_map.keys()) + 1
        lineno_complexity = float(lineno_complexity) / length
        return lineno_complexity
