# File name: instruction.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


from enum import Enum

from src.globals import *


class InstructionType(Enum):
    __order__ = 'RETURN'
    RETURN = 1


class Instruction(object):
    """
    Instruction within a block.

    instruction_type: obj
        InstructionType of instruction to enable specific functionality.
    referenced: set(str)
        Variables referenced in the instruction.
    defined: set(str)
        Variables defined in the block.
    lineno: int
        Line number.
    control: int
        Line number controling this instruction.
    """

    def __init__(self, lineno):
        self.instruction_type = None
        self.lineno = lineno
        self.referenced = set()
        self.defined = set()
        self.control = None

    def __str__(self):
        string = '#%d | ' %self.lineno
        if self.control:
            string += '(#%d) ' %(self.control)
        if self.referenced:
            string += 'REF(%s) ' %(', '.join(self.referenced))
        if self.defined:
            string += 'DEF(%s) ' %(', '.join(self.defined))
        if self.instruction_type:
            string += '- %s' %(self.instruction_type.name.lower())
        return string

    def __eq__(self, other):
        if not other or not isinstance(other, self.__class__):
            return False

        return (self.instruction_type == other.instruction_type and
                self.lineno == other.lineno and
                self.referenced == other.referenced and
                self.defined == other.defined)

    def __ne__(self, other):
        return not self == other
