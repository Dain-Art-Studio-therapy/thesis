# File name: slice.py
# Author: Nupur Garg
# Date created: 2/20/2017
# Python Version: 3.5


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

        # Returns set of line numbers instructions.
        return visited

    # Creates a CFG from a set of instructions in sorted blocks.
    def _generate_cfg_slice(self, sorted_blocks, slice_instrs):
        block_map = {} # function block number : slice block number
        slice_cfg = BlockList()

        for block in sorted_blocks:
            # Get all instructions in this block that are in the slice.
            linenos = block.get_instruction_linenos().intersection(slice_instrs)

            # Copy block if there are instructions to copy or it's directional.
            if linenos:
                # Create a copy of the block.
                if not block_map:
                    curr_bloc = FunctionBlock(self.func.label)
                    slice_cfg.add(curr_bloc)
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

        # # TODO: REMOVE - prints for debugging
        # cfg_temp = BlockList()
        # cfg_temp.add(self.func)
        # print("")
        # print("")
        # for key, value in block_map.items():
        #     print("%s\t\t%s" %(key, value.label))
        # print("")
        # print(slice_cfg)

        return slice_cfg

    # Gets a slice for the function block for the given line number.
    def get_slice(self, start_lineno):
        sorted_blocks = self.func.get_sorted_blocks()
        instrs = self._get_instructions_in_slice(start_lineno)
        slice_cfg = self._generate_cfg_slice(sorted_blocks, instrs)
        return slice_cfg

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
