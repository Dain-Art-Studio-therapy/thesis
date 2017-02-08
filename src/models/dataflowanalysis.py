# File name: dataflowanalysis.py
# Author: Nupur Garg
# Date created: 1/31/2017
# Python Version: 3.5


import copy

from src.globals import *
from src.models.blockinfo import *


class IterativeDataflowAnalysis(ABC):
    """
    Abstract class to perform dataflow analysis.

    block_info_type: BlockInformation
        BlockInformation class.
    """

    def __init__(self, block_info_type):
        self.block_info_type = block_info_type

    # Performs the analysis.
    def analyze(self, func_block):
        # Initialize FunctionBlock.
        info = FunctionBlockInformation()
        info.init(func_block, self.block_info_type)

        # Compute gen and kill maps.
        func_gen = self._compute_func_gen(info)
        self._compute_gen_kill(info, func_gen)

        # Compute in and out maps.
        info_cpy = None
        while info != info_cpy:
            info_cpy = copy.deepcopy(info)
            self._compute_info(info, func_block)

        return info

    # Compute the gen map for a function.
    def _compute_func_gen(self, func_block_info):
        func_gen = {}
        for block, info in func_block_info.blocks():
            for instruction in block.get_instructions():
                for variable in instruction.defined:
                    if not variable in func_gen:
                        func_gen[variable] = set()
                    func_gen[variable].add((block.label, instruction.lineno))
        return func_gen

    # Compute gen and kill maps for each block.
    def _compute_gen_kill(self, func_block_info, func_gen):
        for block, info in func_block_info.blocks():
            # Generate gen map for given block.
            for instruction in block.get_instructions():
                for variable in instruction.defined:
                    if not variable in info.gen:
                        info.gen[variable] = set()
                    info.gen[variable].add((block.label, instruction.lineno))

                # Generate gen and kill map for given instruction.
                instr_info = func_block_info.get_instruction_info(instruction.lineno)
                instr_info.gen = {var: set([(block.label, instruction.lineno)])
                                  for var in instruction.defined}
                instr_info.kill = BlockInformation.diff_common_keys(func_gen, instr_info.gen)

            # Generate kill map for given block.
            info.kill = BlockInformation.diff_common_keys(func_gen, info.gen)
 
    # Computes the information specific to the iterative data flow.
    @abstractmethod
    def _compute_info(self, func_block_info, func_block):
        pass


class ReachingDefinitionsAnalysis(IterativeDataflowAnalysis):
    """
    Determines reaching definitions for each class.
    """

    def __init__(self):
        super(self.__class__, self).__init__(ReachingDefinitions)

    def _compute_info(self, func_block_info, func_block):
        for block in func_block.get_sorted_blocks():
            info = func_block_info.get_block_info(block)

            # Calculate in: Union all predecessors out.
            for func_name, predecessor in block.predecessors.items():
                predecessor_info = func_block_info.get_block_info(predecessor)
                info.in_node = BlockInformation.union(predecessor_info.out_node, info.in_node)

            # Calculate out: gen UNION (in - kill)
            in_sub_kill = BlockInformation.sub(info.in_node, info.kill)
            info.out_node = BlockInformation.union(info.gen, in_sub_kill)

            # Calculate block information for all instructions in the block.
            prev_info = info.in_node
            for lineno, instr in block.instructions.items():
                instr_info = func_block_info.get_instruction_info(lineno)
                instr_info.in_node = prev_info

                in_sub_kill = BlockInformation.sub(instr_info.in_node, instr_info.kill)
                instr_info.out_node = BlockInformation.union(instr_info.gen, in_sub_kill)
                prev_info = instr_info.out_node
