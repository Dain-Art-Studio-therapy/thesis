# File name: test_generatecfg.py
# Author: Nupur Garg
# Date created: 12/26/2016
# Date last modified: 12/26/2016
# Python Version: 3.5


from __future__ import print_function
import unittest
import ast

from src.generatecfg import CFGGenerator


class TestGenerateCFG(unittest.TestCase):

   def setUp(self):
      self.generator = CFGGenerator(False)

   def _generate_cfg(self, source):
      node = ast.parse(source)
      cfg = self.generator.generate(node)
      return cfg

   def test_simple_str(self):
      source = ('string1 = "hi"\n'
                'string2, string3 = string1, "hello"\n'
                'print(string1)')
      cfg = self._generate_cfg(source)
      block = cfg.block_list[0]

      self.assertEqual(block.instructions[1].referenced, set())
      self.assertEqual(block.instructions[1].defined, set(['string1']))
      self.assertEqual(block.instructions[2].referenced, set(['string1']))
      self.assertEqual(block.instructions[2].defined, set(['string2', 'string3']))
      self.assertEqual(block.instructions[3].referenced, set(['print', 'string1']))
      self.assertEqual(block.instructions[3].defined, set())

   def test_simple_loop(self):
      source = ('favs = ["berry", "apple"]\n'
                'name = "peter"\n'
                'for item in favs:\n'
                '   print("%s likes %s" % (name, item))')
      cfg = self._generate_cfg(source)
      block = cfg.block_list[0]

      self.assertEqual(block.instructions[1].defined, set(['favs']))
      self.assertEqual(block.instructions[2].defined, set(['name']))
      self.assertEqual(block.instructions[3].referenced, set(['favs']))
      self.assertEqual(block.instructions[3].defined, set(['item']))
      self.assertEqual(block.instructions[4].referenced, set(['print', 'item', 'name']))


if __name__ == '__main__':
   unittest.main()
