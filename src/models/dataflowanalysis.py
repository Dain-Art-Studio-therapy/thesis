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
            self._compute_info(func_block, info)

        return info

    # Compute the gen map for a function.
    def _compute_func_gen(self, func_block_info):
        func_gen = {}
        for block, info in func_block_info.items():
            for instruction in block.get_instructions():
                for variable in instruction.defined:
                    if not variable in func_gen:
                        func_gen[variable] = set()
                    func_gen[variable].add(instruction.lineno)
        return func_gen

    # Compute gen and kill maps for each block.
    def _compute_gen_kill(self, func_block_info, func_gen):
        for block, info in func_block_info.items():
            # Generate gen map for given block.
            for instruction in block.get_instructions():
                for variable in instruction.defined:
                    if not variable in info.gen:
                        info.gen[variable] = set()
                    info.gen[variable].add(instruction.lineno)

            # Generate kill map for given block.
            info.kill = BlockInformation.diff_common_keys(func_gen, info.gen)
 
    # Computes the information specific to the iterative data flow.
    @abstractmethod
    def _compute_info(self, func_block, func_block_info):
        pass


class ReachingDefinitionsAnalysis(IterativeDataflowAnalysis):
    """
    Determines reaching definitions for each class.
    """

    def __init__(self):
        super(self.__class__, self).__init__(ReachingDefinitions)

    def _compute_info(self, func_block, func_block_info):
        for block in func_block.get_sorted_blocks():
            info = func_block_info.get_block_info(block)

            # Calculate in: Union all predecessors out.
            for func_name, predecessor in block.predecessors.items():
                predecessor_info = func_block_info.get_block_info(predecessor)
                info.in_block = BlockInformation.union(predecessor_info.out_block, info.in_block)

            # Calculate out: gen UNION (in - kill)
            in_sub_kill = BlockInformation.sub(info.in_block, info.kill)
            info.out_block = BlockInformation.union(info.gen, in_sub_kill)
