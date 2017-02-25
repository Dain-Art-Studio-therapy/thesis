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

    def _get_instrs_slice(self, source, lineno):
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(lineno)
        return instrs

    def _get_cfg_slice(self, source, lineno):
        slicemethod = self._get_slice_class(source)
        sorted_blocks = slicemethod.func.get_sorted_blocks()
        instrs = slicemethod._get_instructions_in_slice(lineno)
        slice_cfg = slicemethod._generate_cfg_slice(sorted_blocks, instrs)
        return slice_cfg

    def _get_slice(self, source, lineno):
        slicemethod = self._get_slice_class(source)
        return slicemethod.get_slice(lineno)

    def assertBlockInstrsEqual(self, block, linenos):
        actual = block.get_instruction_linenos()
        if linenos is None:
            self.assertFalse(actual)
        else:
            self.assertEqual(actual, set(linenos))

    def assertBlockSuccessorsEqual(self, block, successors):
        actual = set(block.successors.keys())
        if successors is None:
            self.assertFalse(actual)
        else:
            self.assertEqual(actual, set(successors))


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
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([13, 12]))

    # Test _get_instructions_in_slice with line 12 as 'a = a'.
    def test_get_instructions_in_slice_a(self):
        source = self._get_conditional_source('a')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([13, 12, 5, 4]))

    # Test _get_instructions_in_slice with line 12 as 'a = b'.
    def test_get_instructions_in_slice_b(self):
        source = self._get_conditional_source('b')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([2, 4, 5, 6, 9, 10, 12, 13]))

    # Test _get_instructions_in_slice with line 12 as 'a = c'.
    def test_get_instructions_in_slice_c(self):
        source = self._get_conditional_source('c')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([2, 3, 4, 5, 6, 7, 8, 12, 13]))

    # Test _get_instructions_in_slice with line 12 as 'a = d'.
    def test_get_instructions_in_slice_d(self):
        source = self._get_conditional_source('d')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([2, 4, 5, 6, 7, 9, 10, 11, 12, 13]))

    # Test _generate_cfg_slice with line 12 as 'a = 5'.
    def test_generate_cfg_slice_5(self):
        source = self._get_conditional_source('5')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockInstrsEqual(funcA, None)

        # If conditional.
        block = funcA.successors['L4']
        self.assertBlockInstrsEqual(block, None)

        # Else conditional.
        block = funcA.successors['L5']
        self.assertBlockInstrsEqual(block, None)

        # Exit block.
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])

    # Test _generate_cfg_slice with line 12 as 'a = a'.
    def test_generate_cfg_slice_a(self):
        source = self._get_conditional_source('a')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [4, 5])

        # If conditional.
        block = funcA.successors['L4']
        self.assertBlockInstrsEqual(block, None)

        # Else conditional.
        block = funcA.successors['L5']
        self.assertBlockInstrsEqual(block, None)

        # Exit block.
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])

    # Test _generate_cfg_slice with line 12 as 'a = b'.
    def test_generate_cfg_slice_b(self):
        source = self._get_conditional_source('b')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [2, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L4']
        self.assertBlockInstrsEqual(block, None)

        # Else conditional.
        block = funcA.successors['L5']
        self.assertBlockInstrsEqual(block, [9, 10])

        # Exit block.
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])

    # Test _generate_cfg_slice with line 12 as 'a = c'.
    def test_generate_cfg_slice_c(self):
        source = self._get_conditional_source('c')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [2, 3, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L4']
        self.assertBlockInstrsEqual(block, [7, 8])

        # Else conditional.
        block = funcA.successors['L5']
        self.assertBlockInstrsEqual(block, None)

        # Exit block.
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])

    # Test get_slice with line 12 as 'a = d'.
    def test_generate_cfg_slice_d(self):
        source = self._get_conditional_source('d')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [2, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L4']
        self.assertBlockInstrsEqual(block, [7])

        # Else conditional.
        block = funcA.successors['L5']
        self.assertBlockInstrsEqual(block, [9, 10, 11])

        # Exit block.
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])

    # python3 -m unittest tests.models.test_slice.TestSliceConditional.test_get_slice_5
    # Test get_slice with line 12 as 'a = 5'.
    def test_get_slice_5(self):
        source = self._get_conditional_source('5')
        funcA = self._get_slice(source, lineno=13)

        # funcA
        self.assertBlockInstrsEqual(funcA, [12, 13])
        self.assertBlockSuccessorsEqual(funcA, None)

    # Test get_slice with line 12 as 'a = a'.
    def test_get_slice_a(self):
        source = self._get_conditional_source('a')
        funcA = self._get_slice(source, lineno=13)

        # funcA
        self.assertBlockInstrsEqual(funcA, [4, 5, 12, 13])
        self.assertBlockSuccessorsEqual(funcA, None)

    # Test get_slice with line 12 as 'a = b'.
    def test_get_slice_b(self):
        source = self._get_conditional_source('b')
        funcA = self._get_slice(source, lineno=13)

        # funcA
        self.assertBlockInstrsEqual(funcA, [2, 4, 5, 6])
        self.assertBlockSuccessorsEqual(funcA, ['L5', 'L6'])

        # funcA successor
        block = funcA.successors['L5']
        self.assertBlockInstrsEqual(block, [9, 10])
        self.assertBlockSuccessorsEqual(block, ['L6'])

        # L4 successor block
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])
        self.assertBlockSuccessorsEqual(block, None)

    # Test get_slice with line 12 as 'a = c'.
    def test_get_slice_c(self):
        source = self._get_conditional_source('c')
        funcA = self._get_slice(source, lineno=13)

        # funcA
        self.assertBlockInstrsEqual(funcA, [2, 3, 4, 5, 6])
        self.assertBlockSuccessorsEqual(funcA, ['L4', 'L6'])

        # funcA successor
        block = funcA.successors['L4']
        self.assertBlockInstrsEqual(block, [7, 8])
        self.assertBlockSuccessorsEqual(block, ['L6'])

        # L4 successor block
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])
        self.assertBlockSuccessorsEqual(block, None)

    # Test get_slice with line 12 as 'a = d'.
    def test_get_slice_d(self):
        source = self._get_conditional_source('d')
        funcA = self._get_slice(source, lineno=13)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [2, 4, 5, 6])
        self.assertBlockSuccessorsEqual(funcA, ['L4', 'L5'])

        # If conditional.
        block = funcA.successors['L4']
        self.assertBlockInstrsEqual(block, [7])
        self.assertBlockSuccessorsEqual(block, ['L6'])

        # Else conditional.
        block = funcA.successors['L5']
        self.assertBlockInstrsEqual(block, [9, 10, 11])
        self.assertBlockSuccessorsEqual(block, ['L6'])

        # Exit block.
        block = block.successors['L6']
        self.assertBlockInstrsEqual(block, [12, 13])
        self.assertBlockSuccessorsEqual(block, None)


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
        instrs = self._get_instrs_slice(source, 9)
        self.assertEqual(instrs, set([2, 9]))

    # Test _get_instructions_in_slice with line 9 as 'print(wpixels)'.
    def test_get_instructions_in_slice_wpixels(self):
        source = self._get_conditional_source('wpixels')
        instrs = self._get_instrs_slice(source, 9)
        self.assertEqual(instrs, set([4, 5, 8, 9]))

    # Test _get_instructions_in_slice with line 9 as 'print(hpixels)'.
    def test_get_instructions_in_slice_hpixels(self):
        source = self._get_conditional_source('hpixels')
        instrs = self._get_instrs_slice(source, 9)
        self.assertEqual(instrs, set([3, 5, 6, 7, 9]))

    # Test get_slice with line 9 as 'print(a)'.
    def test_get_slice_a(self):
        source = self._get_conditional_source('a')
        funcA = self._get_cfg_slice(source, lineno=9)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [2])

        # Guard block 1.
        guard_block_1 = funcA.successors['L7']
        self.assertBlockInstrsEqual(guard_block_1, None)

        # Body block 1.
        body_block_1 = guard_block_1.successors['L8']
        self.assertBlockInstrsEqual(body_block_1, None)

        # Guard block 2.
        guard_block_2 = body_block_1.successors['L9']
        self.assertBlockInstrsEqual(guard_block_2, None)

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockInstrsEqual(guard_block_2, None)

        # Exit block 2.
        exit_block_2 = guard_block_2.successors['L11']
        self.assertBlockInstrsEqual(exit_block_2, None)

        # Exit block 2.
        exit_block_1 = guard_block_1.successors['L12']
        self.assertBlockInstrsEqual(exit_block_1, [9])

    # python3 -m unittest tests.models.test_slice.TestSliceLoops.test_generate_cfg_slice_wpixels
    # Test _generate_cfg_slice with line 9 as 'print(wpixels)'.
    def test_generate_cfg_slice_wpixels(self):
        source = self._get_conditional_source('wpixels')
        funcA = self._get_cfg_slice(source, lineno=9)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [4])

        # Guard block 1.
        guard_block_1 = funcA.successors['L7']
        self.assertBlockInstrsEqual(guard_block_1, [5])

        # Body block 1.
        body_block_1 = guard_block_1.successors['L8']
        self.assertBlockInstrsEqual(body_block_1, None)

        # Guard block 2.
        guard_block_2 = body_block_1.successors['L9']
        self.assertBlockInstrsEqual(guard_block_2, None)

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockInstrsEqual(body_block_2, None)

        # Exit block 2.
        exit_block_2 = guard_block_2.successors['L11']
        self.assertBlockInstrsEqual(exit_block_2, [8])

        # Exit block 2.
        exit_block_1 = guard_block_1.successors['L12']
        self.assertBlockInstrsEqual(exit_block_1, [9])

    # Test _generate_cfg_slice with line 9 as 'print(hpixels)'.
    def test_generate_cfg_slice_hpixels(self):
        source = self._get_conditional_source('hpixels')
        funcA = self._get_cfg_slice(source, lineno=9)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [3])

        # Guard block 1.
        guard_block_1 = funcA.successors['L7']
        self.assertBlockInstrsEqual(guard_block_1, [5])

        # Body block 1.
        body_block_1 = guard_block_1.successors['L8']
        self.assertBlockInstrsEqual(body_block_1, None)

        # Guard block 2.
        guard_block_2 = body_block_1.successors['L9']
        self.assertBlockInstrsEqual(guard_block_2, [6])

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockInstrsEqual(body_block_2, [7])

        # Exit block 2.
        exit_block_2 = guard_block_2.successors['L11']
        self.assertBlockInstrsEqual(exit_block_2, None)

        # Exit block 2.
        exit_block_1 = guard_block_1.successors['L12']
        self.assertBlockInstrsEqual(exit_block_1, [9])

    # Test _generate_cfg_slice with line 9 as 'print(a)'.
    def test_generate_cfg_slice_a(self):
        source = self._get_conditional_source('a')
        funcA = self._get_slice(source, lineno=9)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [2, 9])
        self.assertBlockSuccessorsEqual(funcA, None)

    # Test get_slice with line 9 as 'print(hpixels)'.
    def test_get_slice_wpixels(self):
        source = self._get_conditional_source('wpixels')
        funcA = self._get_slice(source, lineno=9)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [4])
        self.assertBlockSuccessorsEqual(funcA, ['L7'])

        # Guard block 1.
        guard_block_1 = funcA.successors['L7']
        self.assertBlockInstrsEqual(guard_block_1, [5])
        self.assertBlockSuccessorsEqual(guard_block_1, ['L11', 'L12'])

        # Body block 1.
        body_block_1 = guard_block_1.successors['L11']
        self.assertBlockInstrsEqual(body_block_1, [8])
        self.assertBlockSuccessorsEqual(body_block_1, ['L7'])

        # Exit block 2.
        exit_block_1 = guard_block_1.successors['L12']
        self.assertBlockInstrsEqual(exit_block_1, [9])
        self.assertBlockSuccessorsEqual(exit_block_1, None)

    # Test get_slice with line 9 as 'print(hpixels)'.
    def test_get_slice_hpixels(self):
        source = self._get_conditional_source('hpixels')
        funcA = self._get_slice(source, lineno=9)

        # Function block.
        self.assertBlockInstrsEqual(funcA, [3])
        self.assertBlockSuccessorsEqual(funcA, ['L7'])

        # Guard block 1.
        guard_block_1 = funcA.successors['L7']
        self.assertBlockInstrsEqual(guard_block_1, [5])
        self.assertBlockSuccessorsEqual(guard_block_1, ['L9', 'L12'])

        # Guard block 2.
        guard_block_2 = guard_block_1.successors['L9']
        self.assertBlockInstrsEqual(guard_block_2, [6])
        self.assertBlockSuccessorsEqual(guard_block_2, ['L7', 'L10'])

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockInstrsEqual(body_block_2, [7])
        self.assertBlockSuccessorsEqual(body_block_2, ['L9'])

        # Exit block 2.
        exit_block_1 = guard_block_1.successors['L12']
        self.assertBlockInstrsEqual(exit_block_1, [9])
        self.assertBlockSuccessorsEqual(exit_block_1, None)


if __name__ == '__main__':
     unittest.main()
