# File name: slice.py
# Author: Nupur Garg
# Date created: 2/20/2017
# Python Version: 3.5


import copy

from src.models.block import FunctionBlock, Block, BlockList
from src.models.blockinfo import FunctionBlockInformation, ReachingDefinitions
from src.models.dataflowanalysis import ReachingDefinitionsAnalysis


class Slice(object):
    """
    Generates a slice for a function block.

    func: obj
        FunctionBlock for the current function.
    info: obj
        FunctionBlockInformation containg ReachingDefinitions for current block.
    """

    def __init__(self, func):
        self.func = func
        analysismethod = ReachingDefinitionsAnalysis()
        self.info = analysismethod.analyze(self.func)

    # Gets set of line numbers in a slice.
    def _get_instructions_in_slice(self, start_lineno):
        visited = set([start_lineno])
        queue = [start_lineno]

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

            # Trace line numbers of control variables.
            if instr.control and instr.control not in visited:
                queue.append(instr.control)

        # Returns set of line numbers instructions.
        return visited

    # Creates a FunctionBlock representing a CFG from a
    # set of instructions in sorted blocks.
    def _generate_cfg_slice(self, sorted_blocks, slice_instrs):
        block_map = {} # function block number : slice block number
        slice_func = FunctionBlock(self.func.label)

        for block in sorted_blocks:
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
        func_copy = None
        while func != func_copy:
            func_copy = copy.deepcopy(func)
            func = self._condense_cfg_helper(func)
        return func

    # Gets a slice for the function block for the given line number.
    def get_slice(self, start_lineno):
        sorted_blocks = self.func.get_sorted_blocks()
        instrs = self._get_instructions_in_slice(start_lineno)
        slice_func = self._generate_cfg_slice(sorted_blocks, instrs)
        slice_func = self.condense_cfg(slice_func)
        return slice_func

    def print_slice_last_statement(self,):
        # Get last statement.
        sorted_blocks = self.func.get_sorted_blocks()
        instr = None
        block_idx = -1
        while instr is None:
            instrs = sorted_blocks[block_idx].get_instructions()
            if instrs:
                instr = instrs[-1]
            block_idx -= 1

        # Get slice from instruction.
        slice_cfg = self.get_slice(instr.lineno)
        print(slice_cfg)
