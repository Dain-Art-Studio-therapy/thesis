# File name: block.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


import collections

from src.globals import *
from src.models.blockinfo import FunctionBlockInformation, ReachingDefinitions
from src.models.counter import Counter
from src.models.dataflowanalysis import ReachingDefinitionsAnalysis
from src.models.instruction import Instruction


class BlockList(object):
    """
    List of blocks.

    _block_list: list(Block)
        List of blocks.
    """

    def __init__(self):
        self._block_list = []

    def __str__(self):
        string = ''
        for block in self._block_list:
            for sorted_block in block.get_sorted_blocks():
                string += '%s\n' %str(sorted_block)
        return string

    # Adds block to block list.
    def add(self, block):
        self._block_list.append(block)

    # Gets the block with the function name.
    def get_func(self, func_name):
        for block in self._block_list:
            if block.label == func_name:
                return block
        return None

    # Returns number of functions in the block list.
    def get_num_funcs(self):
        return len(self._block_list)

    # Calculates reaching definitions for each FuctionBlock.
    def get_reaching_definitions(self):
        return self._perform_dataflow_analysis(ReachingDefinitionsAnalysis())

    # Performs IterativeDataflowAnalysis on each FunctionBlock.
    # Returns {FunctionBlock : FunctionBlockInformation}
    def _perform_dataflow_analysis(self, analysis_class):
        return {func_block.label: analysis_class.analyze(func_block)
                for func_block in self._block_list}

    # Prints a slice calculated on the last statement of the functions.
    def print_slice_last_statement(self):
        reaching_defs = self.get_reaching_definitions()
        for func_name, info in reaching_defs.items():
            func = self.get_func(func_name)

            # Get last statement.
            sorted_blocks = func.get_sorted_blocks()
            instr = sorted_blocks[-1].get_instructions()[-1]

            # Get slice from instruction.
            slice_instrs = self.get_slice(instr.lineno, func, info)
            for instr in slice_instrs:
                print(instr)
        return None

    # Get slice from instruction.
    def get_slice(self, start_lineno, func, reaching_def):
        sorted_blocks = func.get_sorted_blocks()
        visited = set([start_lineno])
        instrs = [start_lineno]
        slice_map = {}

        # Get all instructions in the slice.
        while instrs:
            # Get instruction and instruction info.
            lineno = instrs.pop()
            instr = reaching_def.get_instruction(lineno)
            instr_info = reaching_def.get_instruction_info(lineno)

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


class BlockInterface(object):
    """
    Abstract class BlockInterface.

    successors: list(Block)
        Successors to block.
    predecessors: list(Block)
        Predecessors to block.
    instructions: list(Instruction)
        Instructions in the block.
    label: str
        Label identifying the block.
    """

    _label_counter = Counter()

    def __init__(self, label):
        self.successors = collections.OrderedDict()
        self.predecessors = collections.OrderedDict()
        self.instructions = {}
        self.label = label

    def __str__(self):
        len_tab = len(self.label)

        # Adds block header.
        string = '%s | \n' %str(self.label)

        # Adds predecessors and successors.
        successors = ' | successors(%s)\n' %(', '.join(self.successors.keys()))
        string += successors.rjust(len_tab + len(successors))
        predecessors = ' | predecessors(%s)\n' %(', '.join(self.predecessors.keys()))
        string += predecessors.rjust(len_tab + len(predecessors))

        # Adds instructions.
        for lineno, instruction in self.instructions.items():
            string += '\t%s\n' %str(instruction)
        return string

    def __eq__(self, other):
        if isinstance(other, self.__class__):
          return self.label == other.label
        return False

    # Getter method for label. Sets label if it hasn't been set.
    @property
    def label(self):
        return self.__label

    # Setter for label.
    @label.setter
    def label(self, label):
        if hasattr(self, '_BlockInterface__label'):
            raise ValueError('\'label\' is immutable')
        self.__label = label

    # Gets an instruction from the block.
    def _get_instruction(self, lineno):
        if lineno not in self.instructions:
            self.instructions[lineno] = Instruction(lineno)
        return self.instructions[lineno]

    # Adds variable reference at line number.
    def add_reference(self, lineno, variable):
        instruction = self._get_instruction(lineno)
        instruction.referenced.add(variable)

    # Adds variable defined at line number.
    def add_definition(self, lineno, variable):
        instruction = self._get_instruction(lineno)
        instruction.defined.add(variable)

    # Adds a block as a successor and this block as its predecessor.
    def add_successor(self, block):
        self.successors[block.label] = block
        block.predecessors[self.label] = self

    # Returns instructions.
    def get_instructions(self):
        sorted_instructions = iter(sorted(self.instructions.items()))
        return [instruction for lineno, instruction in sorted_instructions]


class Block(BlockInterface):
    """
    Block representing body of the function within a CFG.
    """

    def __init__(self):
        super(self.__class__, self).__init__(self._get_label())

    # Returns next available label.
    def _get_label(self):
        return 'L%d' %Block._label_counter.increment()


class FunctionBlock(BlockInterface):
    """
    Block representing start of a function within a CFG.
    """

    def __init__(self, label):
        super(self.__class__, self).__init__(label)

    # Gets topologically sorted blocks.
    def get_sorted_blocks(self):
        visited = set()
        sorted_blocks = []
        self._topological_sort_helper(sorted_blocks, visited, self)
        return sorted_blocks

    # Helper method to topologically sort blocks.
    def _topological_sort_helper(self, sorted_blocks, visited, current):
        visited.add(current.label)
        for key in reversed(current.successors.keys()):
            successor = current.successors[key]
            if successor.label not in visited:
                self._topological_sort_helper(sorted_blocks, visited, successor)
        sorted_blocks.insert(0, current)
