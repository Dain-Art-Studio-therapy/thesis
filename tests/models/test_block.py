# File name: test_block.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Date last modified: 12/25/2016
# Python Version: 3.5


from __future__ import print_function
import unittest

from src.models.block import Block


class TestBlock(unittest.TestCase):

   def setUp(self):
      self.block1 = Block()
      self.block2 = Block()
      self.block3 = Block()

   def test_labels(self):
      block_label1 = int(self.block1.label[1:])
      block_label2 = int(self.block2.label[1:])
      self.assertEqual(block_label2 - block_label1, 1)

   def test_add_successor(self):
      self.block1.add_successor(self.block2)
      self.block1.add_successor(self.block3)
      self.assertEqual(self.block1.successors, [self.block2, self.block3])
      self.assertEqual(self.block2.predecessors, [self.block1])
      self.assertEqual(self.block3.predecessors, [self.block1])

if __name__ == '__main__':
   unittest.main()
