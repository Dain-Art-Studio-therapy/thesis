# File name: test_block.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


import unittest
import ast

from src.globals import *
from src.models.block import Block, FunctionBlock
from src.models.instruction import Instruction
from src.generatecfg import CFGGenerator


# Test Block class.
class TestBlock(unittest.TestCase):

    def setUp(self):
        self.block1 = Block()
        self.block2 = Block()
        self.block3 = Block()

    def test_labels(self):
        block_label1 = int(self.block1.label[1:])
        block_label2 = int(self.block2.label[1:])
        self.assertEqual(block_label2 - block_label1, 1)

        # Ensure error when trying to reset label.
        with self.assertRaises(ValueError) as context:
            self.block1.label = 'error_label'

    def test_add_reference(self):
        self.block1.add_reference(lineno=1, variable='varA')
        self.assertEqual(self.block1._instructions[1].referenced, set(['varA']))
        self.assertFalse(self.block1._instructions[1].defined)
        self.assertEqual(len(self.block1.get_instructions()), 1)
        self.assertEqual(set(self.block1._instructions.keys()), set([1]))

        self.block1.add_reference(lineno=2, variable='varA')
        self.block1.add_reference(lineno=2, variable='varB')
        self.assertEqual(self.block1._instructions[2].referenced, set(['varA', 'varB']))
        self.assertFalse(self.block1._instructions[2].defined)
        self.assertEqual(len(self.block1.get_instructions()), 2)
        self.assertEqual(set(self.block1._instructions.keys()), set([1, 2]))

    def test_add_definition(self):
        self.block1.add_definition(lineno=1, variable='varB')
        self.assertFalse(self.block1._instructions[1].referenced)
        self.assertEqual(self.block1._instructions[1].defined, set(['varB']))
        self.assertEqual(len(self.block1.get_instructions()), 1)
        self.assertEqual(set(self.block1._instructions.keys()), set([1]))

        self.block1.add_definition(lineno=2, variable='varA')
        self.block1.add_definition(lineno=2, variable='varC')
        self.assertFalse(self.block1._instructions[2].referenced)
        self.assertEqual(self.block1._instructions[2].defined, set(['varA', 'varC']))
        self.assertEqual(len(self.block1.get_instructions()), 2)
        self.assertEqual(set(self.block1._instructions.keys()), set([1, 2]))

    def test_method_add_instruction(self):
        self.skipTest('TODO: Need to complete')

    def test_add_successor(self):
        self.block1.add_successor(self.block2)
        self.block1.add_successor(self.block3)
        self.assertEqual(list(self.block1.successors), [self.block2.label, self.block3.label])
        self.assertEqual(list(self.block2.predecessors), [self.block1.label])
        self.assertEqual(list(self.block3.predecessors), [self.block1.label])

    def test_add_predecessor(self):
        self.skipTest('TODO: Need to complete')

    def test_get_instruction(self):
        self.skipTest('TODO: Need to complete')

    def test_get_instruction_linenos(self):
        self.skipTest('TODO: Need to complete')

    def test_get_instructions(self):
        self.block1.add_reference(lineno=2, variable='varA')
        self.block1.add_definition(lineno=1, variable='varA')

        instructions = self.block1.get_instructions()
        self.assertEqual(instructions[0].lineno, 1)
        self.assertEqual(instructions[1].lineno, 2)


# Tests FunctionBlock class.
class TestFunctionBlock(unittest.TestCase):

    def setUp(self):
        self.func_block1 = FunctionBlock('func1')

    def test_labels(self):
        self.assertEqual(self.func_block1.label, 'func1')
        with self.assertRaises(ValueError) as context:
            self.func_block1.label = 'error_label'

    def test_get_sorted_blocks(self):
        Block._label_counter.reset()
        source = ('def funcA():\n'
                  '    integers = [[1, 2], [3, 4]]\n'
                  '    for numbers in integers:\n'
                  '        for integer in numbers:\n'
                  '            print("%d " %integer)')

        generator = CFGGenerator(False)
        node = ast.parse(source)
        cfg = generator.generate(node)
        funcA = cfg.get_func('funcA')
        sorted_blocks = funcA.get_sorted_blocks()

        self.assertEqual(sorted_blocks[0].label, 'funcA')
        self.assertEqual(sorted_blocks[1].label, 'L1')
        self.assertEqual(sorted_blocks[2].label, 'L2')
        self.assertEqual(sorted_blocks[3].label, 'L4')
        self.assertEqual(sorted_blocks[4].label, 'L5')
        self.assertEqual(sorted_blocks[5].label, 'L6')
        self.assertEqual(sorted_blocks[6].label, 'L3')

    def test_get_cyclomatic_complexity(self):
        Block._label_counter.reset()
        source = ('def funcA():\n'              # line 1
                  '     i = 3\n'                # line 2
                  '     i = j = i + 1\n'        # line 3
                  '     a = j + 2\n'            # line 4
                  '     while a > 0:\n'         # line 5
                  '         i = i + 1\n'        # line 6
                  '         j = j - 1\n'        # line 7
                  '         if i != j:\n'       # line 8
                  '             a = a - 1\n'    # line 9
                  '         i = i + 1')         # line 10

        generator = CFGGenerator(False)
        node = ast.parse(source)
        cfg = generator.generate(node)
        funcA = cfg.get_func('funcA')
        sorted_blocks = funcA.get_sorted_blocks()

        self.assertEqual(funcA._get_num_nodes(sorted_blocks), 6)
        self.assertEqual(funcA._get_num_edges(sorted_blocks), 7)
        self.assertEqual(funcA._get_num_exits(sorted_blocks, 6), 3)
        self.assertEqual(funcA.get_cyclomatic_complexity(), 7)


if __name__ == '__main__':
    unittest.main()
