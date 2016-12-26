# File name: block.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Date last modified: 12/25/2016
# Python Version: 3.5


# TODO(ngarg): Should I prevent 'label' from being set by others.
#              Options - '@property, @label.setter' or '__setattr__'
# TODO(ngarg): Determine if I need Label() class.


from __future__ import print_function

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
         string += '%s\n' %str(block)
      return string

   def add(self, block):
      self.block_list.append(block)


class Block(object):
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

   _count_label = 0

   def __init__(self):
      self.successors = []
      self.predecessors = []
      self.instructions = []
      self.referenced = set([])
      self.defined = set([])
      self.label = self._get_label()

   def __str__(self):
      string = '%s | ' %str(self.label)
      if self.referenced:
         string += 'REF(%s) ' %(', '.join(self.referenced))
      if self.defined:
         string += 'DEF(%s)' %(', '.join(self.defined))
      string += '\n'

      for instruction in self.instructions:
         string += '\t%s\n' %str(instruction)
      return string

   def __eq__(self, other):
      if isinstance(other, self.__class__):
        return self.label == other.label
      return False

   # Returns next available label.
   def _get_label(self):
      Block._count_label += 1
      return "L%d" %Block._count_label

   # Adds a block as a successor and this block as its predecessor.
   def add_successor(self, block):
      self.successors.append(block)
      block.predecessors.append(self)

   # Adds an instruction to the block.
   def add_instruction(self, instruction):
      self.instructions.append(instruction)
      self.referenced.update(instruction.referenced)
      self.defined.update(instruction.defined)
