# File name: block.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


from __future__ import print_function
import collections

from src.models.counter import Counter
from src.models.instruction import Instruction


class BlockList(object):
    """
    List of blocks.

    block_list: list(Block)
        List of blocks.
    """

    def __init__(self):
        self.block_list = []

    def __str__(self):
        string = ''
        for block in self.block_list:
            for sorted_block in block.get_sorted_blocks():
                string += '%s\n' %str(sorted_block)
        return string

    def add(self, block):
        self.block_list.append(block)


class BlockInterface(object):
    """
    Block within a CFG.

    successors: list(Block)
        Successors to block.
    predecessors: list(Block)
        Predecessors to block.
    instructions: list(Instruction)
        Instructions in the block.
    referenced: set(str)
        Variables referenced in the block.
    defined: set(str)
        Variables defined in the block.
    label: str
        Label identifying the block.
    """

    _label_counter = Counter()

    def __init__(self, label):
        self.successors = collections.OrderedDict()
        self.predecessors = collections.OrderedDict()
        self.instructions = {}
        self.referenced = set([])
        self.defined = set([])
        self.label = label

    def __str__(self):
        len_tab = len(self.label)

        # Adds block header.
        string = '%s | ' %str(self.label)
        if self.referenced:
            string += 'REF(%s) ' %(', '.join(self.referenced))
        if self.defined:
            string += 'DEF(%s)' %(', '.join(self.defined))
        string += '\n'

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

    # Returns next available label.
    def _get_label(self):
        return 'L%d' %Block._label_counter.increment()

    # Gets an instruction from the block.
    def _get_instruction(self, lineno):
        if lineno not in self.instructions:
            self.instructions[lineno] = Instruction(lineno)
        return self.instructions[lineno]

    # Adds variable reference at line number.
    def add_reference(self, lineno, variable):
        instruction = self._get_instruction(lineno)
        instruction.referenced.add(variable)
        self.referenced.add(variable)

    # Adds variable defined at line number.
    def add_definition(self, lineno, variable):
        instruction = self._get_instruction(lineno)
        instruction.defined.add(variable)
        self.defined.add(variable)

    # Adds a block as a successor and this block as its predecessor.
    def add_successor(self, block):
        self.successors[block.label] = block
        block.predecessors[self.label] = self


class Block(BlockInterface):
    """
    General Block within a CFG.
    """

    def __init__(self):
        super(self.__class__, self).__init__(self._get_label())

    # Returns next available label.
    def _get_label(self):
        return 'L%d' %Block._label_counter.increment()


class FunctionBlock(BlockInterface):
    """
    FunctionBlock within a CFG.
    """

    def __init__(self, label):
        super(self.__class__, self).__init__(label)

    def get_sorted_blocks(self):
        visited = set()
        sorted_blocks = []
        self._topological_sort_helper(sorted_blocks, visited, self)
        return sorted_blocks

    def _topological_sort_helper(self, sorted_blocks, visited, current):
        visited.add(current.label)
        for key in reversed(current.successors.keys()):
            successor = current.successors[key]
            if successor.label not in visited:
                self._topological_sort_helper(sorted_blocks, visited, successor)
        sorted_blocks.insert(0, current)
