# File name: test_slice.py
# Author: Nupur Garg
# Date created: 2/22/2017
# Python Version: 3.5


import unittest
import ast

from src.globals import *
from src.generatecfg import CFGGenerator
from src.models.slice import *
from src. models.block import BlockList


# Framework for testing Slice class.
class TestSlice(unittest.TestCase):

    def setUp(self):
        Block._label_counter.reset()

    def _generate_cfg(self, source):
        node = ast.parse(source)
        generator = CFGGenerator(False)
        return generator.generate(node)

    def _get_slice_class(self, source):
        cfg = self._generate_cfg(source)
        func = cfg.get_func('funcA')
        return Slice(func)


# Tests conditionals with Slice class.
class TestSliceConditional(TestSlice):

    def _get_conditional_source(self, var):
        source = ('def funcA():\n'              # line 1
                  '     b = 1\n'                # line 2
                  '     c = 2\n'                # line 3
                  '     d = 3\n'                # line 4
                  '     a = d\n'                # line 5
                  '     if a > 2:\n'            # line 6
                  '         d = b + d\n'        # line 7
                  '         c = b + d\n'        # line 8
                  '     else:\n'                # line 9
                  '         b = b + 1\n'        # line 10
                  '         d = b + 1\n'        # line 11
                  '     a = %s\n'               # line 12
                  '     print(a)\n' %var)       # line 13
        return source

    # Test _get_instructions_in_slice with line 12 as 'a = 5'.
    def test_get_instructions_in_slice_5(self):
        source = self._get_conditional_source('5')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(13)
        self.assertEqual(instrs, set([13, 12]))

    # Test _get_instructions_in_slice with line 12 as 'a = a'.
    def test_get_instructions_in_slice_a(self):
        source = self._get_conditional_source('a')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(13)
        self.assertEqual(instrs, set([13, 12, 5, 4]))

    # Test _get_instructions_in_slice with line 12 as 'a = b'.
    def test_get_instructions_in_slice_b(self):
        source = self._get_conditional_source('b')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(13)
        self.assertEqual(instrs, set([2, 10, 12, 13]))

    # Test _get_instructions_in_slice with line 12 as 'a = c'.
    def test_get_instructions_in_slice_c(self):
        source = self._get_conditional_source('c')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(13)
        self.assertEqual(instrs, set([2, 3, 4, 7, 8, 12, 13]))

    # Test _get_instructions_in_slice with line 12 as 'a = d'.
    def test_get_instructions_in_slice_d(self):
        source = self._get_conditional_source('d')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(13)
        self.assertEqual(instrs, set([2, 4, 7, 10, 11, 12, 13]))

    # Test get_slice with line 12 as 'a = 5'.
    def test_get_slice_5(self):
        source = self._get_conditional_source('5')
        slicemethod = self._get_slice_class(source)
        slice_cfg = slicemethod.get_slice(13)

        # funcA
        funcA = slice_cfg.get_func('funcA')
        instrs = funcA.get_instruction_linenos()
        self.assertEqual(instrs, set([12, 13]))
        self.assertFalse(funcA.successors)

    # Test get_slice with line 12 as 'a = a'.
    def test_get_slice_a(self):
        source = self._get_conditional_source('a')
        slicemethod = self._get_slice_class(source)
        slice_cfg = slicemethod.get_slice(13)
        self.skipTest('TODO: Need to complete')

    # Test get_slice with line 12 as 'a = b'.
    def test_get_slice_b(self):
        source = self._get_conditional_source('b')
        slicemethod = self._get_slice_class(source)
        slice_cfg = slicemethod.get_slice(13)

        # funcA
        funcA = slice_cfg.get_func('funcA')
        instrs = funcA.get_instruction_linenos()
        self.assertEqual(instrs, set([2]))

        # funcA successor
        block = funcA.successors['L4']
        instrs = block.get_instruction_linenos()
        self.assertEqual(instrs, set([10]))

        # L4 successor block
        block = block.successors['L5']
        instrs = block.get_instruction_linenos()
        self.assertEqual(instrs, set([12, 13]))

    # Test get_slice with line 12 as 'a = c'.
    def test_get_slice_c(self):
        source = self._get_conditional_source('c')
        slicemethod = self._get_slice_class(source)
        slice_cfg = slicemethod.get_slice(13)

        # funcA
        funcA = slice_cfg.get_func('funcA')
        instrs = funcA.get_instruction_linenos()
        self.assertEqual(instrs, set([2, 3, 4]))

        # funcA successor
        block = funcA.successors['L4']
        instrs = block.get_instruction_linenos()
        self.assertEqual(instrs, set([7, 8]))

        # L4 successor block
        block = block.successors['L5']
        instrs = block.get_instruction_linenos()
        self.assertEqual(instrs, set([12, 13]))

    # Test get_slice with line 12 as 'a = d'.
    def test_get_slice_d(self):
        source = self._get_conditional_source('d')
        slicemethod = self._get_slice_class(source)
        slice_cfg = slicemethod.get_slice(13)

        # funcA
        funcA = slice_cfg.get_func('funcA')
        instrs = funcA.get_instruction_linenos()
        self.assertEqual(instrs, set([2, 4]))

        # funcA successor
        block = funcA.successors['L4']
        instrs = block.get_instruction_linenos()
        self.assertEqual(instrs, set([7]))

        # funcA successor
        block = funcA.successors['L5']
        instrs = block.get_instruction_linenos()
        self.assertEqual(instrs, set([10, 11]))

        # L4 successor block
        block = block.successors['L6']
        instrs = block.get_instruction_linenos()
        self.assertEqual(instrs, set([12, 13]))


# Tests loops with Slice class.
class TestSliceLoops(TestSlice):

    def _get_conditional_source(self, var):
        source = ('def funcA():\n'                      # line 1
                  '     a = 5\n'                        # line 2
                  '     hpixels = 5\n'                  # line 3
                  '     wpixels = 10\n'                 # line 4
                  '     for y in range(5):\n'           # line 5
                  '         for x in range(2):\n'       # line 6
                  '             hpixels += 1\n'         # line 7
                  '         wpixels += 1\n'             # line 8
                  '     print(%s)\n' %var)              # line 9
        return source

    # Test _get_instructions_in_slice with line 9 as 'print(a)'.
    def test_get_instructions_in_slice_a(self):
        source = self._get_conditional_source('a')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(9)
        self.assertEqual(instrs, set([2, 9]))

    # Test _get_instructions_in_slice with line 9 as 'print(hpixels)'.
    def test_get_instructions_in_slice_hpixels(self):
        source = self._get_conditional_source('hpixels')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(9)
        self.assertEqual(instrs, set([3, 7, 9]))

    # Test get_slice with line 9 as 'print(a)'.
    def test_get_slice_a(self):
        source = self._get_conditional_source('a')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod.get_slice(9)
        self.skipTest('TODO: Need to complete')

    # Test get_slice with line 9 as 'print(a)'.
    def test_get_slice_hpixels(self):
        source = self._get_conditional_source('hpixels')
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod.get_slice(9)
        self.skipTest('TODO: Need to complete')


if __name__ == '__main__':
     unittest.main()
