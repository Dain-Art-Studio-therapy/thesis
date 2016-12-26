# File name: instruction.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Date last modified: 12/25/2016
# Python Version: 3.5


from __future__ import print_function


class Instruction(object):
   """
   Instruction within a block.

   referenced: set(str)
      Variables referenced in the instruction.
   defined: set(str)
      Variables defined in the block.
   lineno: int
      Line number.
   """

   def __init__(self, lineno):
      self.lineno = lineno
      self.referenced = set()
      self.defined = set()

   def __str__(self):
      string = '#%d | ' %self.lineno
      if self.referenced:
         string += 'REF(%s) ' %(', '.join(self.referenced))
      if self.defined:
         string += 'DEF(%s)' %(', '.join(self.defined))
      return string
