# File name: test_block.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


from __future__ import print_function
import unittest

from src.models.block import Block, FunctionBlock
from src.models.instruction import Instruction


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

    def test_add_successor(self):
        self.block1.add_successor(self.block2)
        self.block1.add_successor(self.block3)
        self.assertEqual(list(self.block1.successors), [self.block2.label, self.block3.label])
        self.assertEqual(list(self.block2.predecessors), [self.block1.label])
        self.assertEqual(list(self.block3.predecessors), [self.block1.label])

    def test_add_instruction(self):
        self.block1.add_reference(lineno=1, variable="varA")
        self.block1.add_definition(lineno=1, variable="varB")
        self.assertEqual(self.block1.referenced, set(["varA"]))
        self.assertEqual(self.block1.defined, set(["varB"]))
        self.assertEqual(len(self.block1.instructions), 1)
        self.assertEqual(set(self.block1.instructions.keys()), set([1]))

        self.block1.add_reference(lineno=2, variable="varA")
        self.block1.add_reference(lineno=2, variable="varB")
        self.block1.add_definition(lineno=2, variable="varC")
        self.assertEqual(self.block1.referenced, set(["varA", "varB"]))
        self.assertEqual(self.block1.defined, set(["varB", "varC"]))
        self.assertEqual(len(self.block1.instructions), 2)
        self.assertEqual(set(self.block1.instructions.keys()), set([1, 2]))


# Tests FunctionBlock class.
class TestFunctionBlock(unittest.TestCase):

    def setUp(self):
        self.funcBlock1 = FunctionBlock('func1')

    def test_labels(self):
        self.assertEqual(self.funcBlock1.label, 'func1')
        with self.assertRaises(ValueError) as context:
            self.funcBlock1.label = 'error_label'

if __name__ == '__main__':
    unittest.main()
