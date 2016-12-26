# File name: generatecfg.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Date last modified: 12/25/2016
# Python Version: 3.5


from __future__ import print_function
import ast


# Visitor to generate CFG.
class CFGGenerator(ast.NodeVisitor):
   """
   Generates a CFG from an AST.

   debug: bool
      Whether to print debug messages.
   """

   def __init__(self, debug):
      self.debug = debug
      self.temp = None

   # Generates CFG.
   def generate(self, node):
      # TODO(ngarg): Initialize variables.
      self.visit(node)
      # TODO(ngarg): Return variables.
      print("returned: ", self.temp)
      return "TEMP"

   def visit_Str(self, node):
      self.temp = "testing"
      print('line %d: (str) "%s"' %(node.lineno, node.s))
