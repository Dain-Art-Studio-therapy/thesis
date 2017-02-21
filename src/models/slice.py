# File name: slice.py
# Author: Nupur Garg
# Date created: 2/20/2017
# Python Version: 3.5


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

    # Gets a slice for the function block for the given line number.
    def get_slice(self, start_lineno):
        sorted_blocks = self.func.get_sorted_blocks()
        visited = set([start_lineno])
        instrs = [start_lineno]
        slice_map = {}

        # Get all instructions in the slice.
        while instrs:
            # Get instruction and instruction info.
            lineno = instrs.pop()
            instr = self.info.get_instruction(lineno)
            instr_info = self.info.get_instruction_info(lineno)

            # Add to slice.
            visited.add(lineno)
            slice_map[instr.lineno] = instr

            # Trace values of referenced values.
            for var in instr.referenced:
                if var in instr_info.in_node:
                    for block_label, lineno in instr_info.in_node[var]:
                        if lineno not in visited:
                            instrs.append(lineno)

        # Generate slice_map from ordered instructions.
        return [slice_map[lineno] for lineno in sorted(visited)]

    def print_slice_last_statement(self,):
        # Get last statement.
        sorted_blocks = self.func.get_sorted_blocks()
        instr = None
        idx = -1
        while instr is None:
            instrs = sorted_blocks[idx].get_instructions()
            if instrs:
                instr = instrs[-1]
            idx -= 1

        # Get slice from instruction.
        slice_instrs = self.get_slice(instr.lineno)
        print('%s (%d)' %(self.func.label, self.func.get_cyclomatic_complexity()))
        for instr in slice_instrs:
            print('\t%s' %instr)
        print('')
