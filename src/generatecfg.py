# File name: generatecfg.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Date last modified: 12/25/2016
# Python Version: 3.5


from __future__ import print_function
import ast

from src.models.block import Block, BlockList


# Visitor to generate CFG.
class CFGGenerator(ast.NodeVisitor):
   """
   Generates a CFG from an AST.

   debug: bool
      Whether to print debug messages.
   """

   def __init__(self, debug):
      self.debug = debug
      self._init_variables()

   def _init_variables(self):
      self.block_list = BlockList()
      self.current_block = None

   # Generates CFG.
   def generate(self, node):
      self._init_variables()
      self.visit(node)
      return self.block_list

   # Module(stmt* body)
   def visit_Module(self, node):
      self.current_block = Block()
      self.block_list.add(self.current_block)
      self.generic_visit(node)

   def visit_Str(self, node):
      self.temp = "testing"
      print('line %d: (str) "%s"' %(node.lineno, node.s))
