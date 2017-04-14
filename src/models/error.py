# File name: error.py
# Author: Nupur Garg
# Date created: 4/13/2017
# Python Version: 3.5


from src.globals import *


class DecomposerError(RuntimeError):
    pass


# File not found error.
class FileNotFoundError(DecomposerError):

    def __init__(self, filename):
        self.message = "{} not found.".format(filename)
        self.filename = filename
        Exception.__init__(self, self.message)


# Else without an if error.
class ElseWithoutIfError(DecomposerError):

    def __init__(self, lineno):
        self.message = "Elif or else without an if on line {}.".format(lineno)
        self.lineno = lineno
        Exception.__init__(self, self.message)