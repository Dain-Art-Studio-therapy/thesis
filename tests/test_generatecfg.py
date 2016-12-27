# File name: test_generatecfg.py
# Author: Nupur Garg
# Date created: 12/26/2016
# Python Version: 3.5


from __future__ import print_function
import unittest
import ast

from src.models.block import Block
from src.generatecfg import CFGGenerator


class TestGenerateCFG(unittest.TestCase):

    def setUp(self):
        Block._label_counter.reset()
        self.generator = CFGGenerator(False)

    def _generate_cfg(self, source):
        node = ast.parse(source)
        cfg = self.generator.generate(node)
        return cfg

    def test_no_code(self):
        source = ''
        cfg = self._generate_cfg(source)
        self.assertEqual(len(cfg.block_list), 0)

    def test_simple_script(self):
        source = 'string = "hi"'
        cfg = self._generate_cfg(source)
        self.assertEqual(len(cfg.block_list), 0)

    def test_simple_str(self):
        source = ('string0 = "hi"\n'
                  'def funcA():\n'
                  '    string1 = "hi"\n'
                  '    string2, string3 = string1, "hello"\n'
                  '    print(string1)')
        cfg = self._generate_cfg(source)
        block = cfg.block_list[0]

        self.assertEqual(block.label, 'funcA')
        self.assertEqual(block.instructions[3].referenced, set())
        self.assertEqual(block.instructions[3].defined, set(['string1']))
        self.assertEqual(block.instructions[4].referenced, set(['string1']))
        self.assertEqual(block.instructions[4].defined, set(['string2', 'string3']))
        self.assertEqual(block.instructions[5].referenced, set(['print', 'string1']))
        self.assertEqual(block.instructions[5].defined, set())

    def test_single_for_loop(self):
        source = ('def funcA():\n'
                  '    favs = ["berry", "apple"]\n'
                  '    name = "peter"\n'
                  '    for item in favs:\n'
                  '        print("%s likes %s" % (name, item))')
        cfg = self._generate_cfg(source)
        func_block = cfg.block_list[0]

        self.assertEqual(func_block.label, 'funcA')
        self.assertEqual(func_block.instructions[2].defined, set(['favs']))
        self.assertEqual(func_block.instructions[3].defined, set(['name']))
        self.assertEqual(list(func_block.successors), ['L1'])

        guard_block = func_block.successors['L1']
        self.assertEqual(guard_block.instructions[4].referenced, set(['favs']))
        self.assertEqual(guard_block.instructions[4].defined, set(['item']))
        self.assertEqual(list(guard_block.predecessors), ['funcA', 'L2'])
        self.assertEqual(list(guard_block.successors), ['L2', 'L3'])

        body_block = guard_block.successors['L2']
        self.assertEqual(body_block.instructions[5].referenced, set(['print', 'item', 'name']))
        self.assertEqual(body_block.instructions[5].defined, set())
        self.assertEqual(list(body_block.predecessors), ['L1'])
        self.assertEqual(list(body_block.successors), ['L1'])

        exit_block = guard_block.successors['L3']
        self.assertFalse(exit_block.instructions)
        self.assertEqual(list(exit_block.predecessors), ['L1'])

    def test_nested_for_loop(self):
        source = ('def funcA():\n'
                  '    integers = [[1, 2], [3, 4]]\n'
                  '    for numbers in integers:\n'
                  '        for integer in numbers:\n'
                  '            print("%d " %integer)')
        cfg = self._generate_cfg(source)
        func_block = cfg.block_list[0]

        self.assertEqual(func_block.label, 'funcA')
        self.assertEqual(func_block.instructions[2].referenced, set())
        self.assertEqual(func_block.instructions[2].defined, set(['integers']))
        self.assertEqual(list(func_block.successors), ['L1'])
        self.assertFalse(func_block.predecessors)

        guard_block_1 = func_block.successors['L1']
        self.assertEqual(guard_block_1.instructions[3].referenced, set(['integers']))
        self.assertEqual(guard_block_1.instructions[3].defined, set(['numbers']))
        self.assertEqual(list(guard_block_1.predecessors), ['funcA', 'L6'])
        self.assertEqual(list(guard_block_1.successors), ['L2', 'L3'])

        body_start_1 = guard_block_1.successors['L2']
        self.assertFalse(body_start_1.instructions)
        self.assertEqual(list(body_start_1.predecessors), ['L1'])
        self.assertEqual(list(body_start_1.successors), ['L4'])

        guard_block_2 = body_start_1.successors['L4']
        self.assertEqual(guard_block_2.instructions[4].referenced, set(['numbers']))
        self.assertEqual(guard_block_2.instructions[4].defined, set(['integer']))
        self.assertEqual(list(guard_block_2.predecessors), ['L2', 'L5'])
        self.assertEqual(list(guard_block_2.successors), ['L5', 'L6'])

        body_2 = guard_block_2.successors['L5']
        self.assertEqual(body_2.instructions[5].referenced, set(['integer', 'print']))
        self.assertEqual(body_2.instructions[5].defined, set())
        self.assertEqual(list(body_2.predecessors), ['L4'])
        self.assertEqual(list(body_2.successors), ['L4'])

        body_end_1 = guard_block_1.predecessors['L6']
        self.assertFalse(body_end_1.instructions)
        self.assertEqual(list(body_end_1.predecessors), ['L4'])
        self.assertEqual(list(body_end_1.successors), ['L1'])

        exit_block = guard_block_1.successors['L3']
        self.assertFalse(exit_block.instructions)
        self.assertEqual(list(exit_block.predecessors), ['L1'])
        self.assertFalse(exit_block.successors)


if __name__ == '__main__':
    unittest.main()
