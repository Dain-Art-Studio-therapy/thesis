# File name: test_slice.py
# Author: Nupur Garg
# Date created: 2/22/2017
# Python Version: 3.5


import unittest
import ast
import copy

from src.globals import *
from src.parser import parse_json
from src.generatecfg import CFGGenerator
from src.models.slice import *
from src.models.block import BlockList
from src.models.instruction import Instruction


# Tests Suggestion class.
class TestSuggestion(unittest.TestCase):

    def setUp(self):
        self.ref_vars = ['ref_var', 'ref_var']
        self.ret_vars = ['ret_var']
        self.types = [SuggestionType.REMOVE_VAR]

    def _generate_suggestions_list(self):
        self.suggestion1 = Suggestion(self.ref_vars, self.ret_vars, self.types, "funcA", start_lineno=1)
        self.suggestion3 = Suggestion(self.ref_vars, self.ret_vars, self.types, "funcA", start_lineno=3)
        self.suggestion35 = Suggestion(self.ref_vars, self.ret_vars, self.types, "funcA", start_lineno=3, end_lineno=5)
        self.suggestion4 = Suggestion(self.ref_vars, self.ret_vars, self.types, "funcA", start_lineno=4)
        self.suggestion4cpy = Suggestion(self.ref_vars, self.ret_vars, self.types, "funcA", start_lineno=4)
        self.suggestions = [self.suggestion4cpy, self.suggestion1,
                            self.suggestion35, self.suggestion4, self.suggestion3]

    def test_init(self):
        suggestion = Suggestion(self.ref_vars, self.ret_vars, self.types, "funcA", start_lineno=1)
        self.assertEqual(suggestion.ref_vars, self.ref_vars)
        self.assertEqual(suggestion.ret_vars, self.ret_vars)
        self.assertEqual(suggestion.types, self.types)
        self.assertEqual(suggestion.start_lineno, 1)
        self.assertEqual(suggestion.end_lineno, 1)

        suggestion = Suggestion(self.ref_vars, self.ret_vars, self.types, "funcA", start_lineno=1, end_lineno=3)
        self.assertEqual(suggestion.ref_vars, self.ref_vars)
        self.assertEqual(suggestion.ret_vars, self.ret_vars)
        self.assertEqual(suggestion.types, self.types)
        self.assertEqual(suggestion.start_lineno, 1)
        self.assertEqual(suggestion.end_lineno, 3)

    def test_sort(self):
        self._generate_suggestions_list()
        self.suggestions.sort()

        self.assertEqual(self.suggestions[0], self.suggestion1)
        self.assertEqual(self.suggestions[1], self.suggestion3)
        self.assertEqual(self.suggestions[2], self.suggestion35)
        self.assertEqual(self.suggestions[3], self.suggestion4cpy)
        self.assertEqual(self.suggestions[4], self.suggestion4)

    def test_sorted(self):
        self._generate_suggestions_list()
        self.suggestions = sorted(self.suggestions)

        self.assertEqual(self.suggestions[0], self.suggestion1)
        self.assertEqual(self.suggestions[1], self.suggestion3)
        self.assertEqual(self.suggestions[2], self.suggestion35)
        self.assertEqual(self.suggestions[3], self.suggestion4cpy)
        self.assertEqual(self.suggestions[4], self.suggestion4)

    def test_str(self):
        self.skipTest('TODO: Implement')


# Framework for testing Slice class.
class TestSlice(unittest.TestCase):

    def setUp(self):
        Block._label_counter.reset()

    def _generate_cfg(self, source):
        node = ast.parse(source)
        generator = CFGGenerator(False)
        return generator.generate(node, source)

    def _get_slice_class(self, source):
        cfg = self._generate_cfg(source)
        func = cfg.get_func('funcA')
        config = parse_json()
        return Slice(func, config)

    def _get_instrs_slice(self, source, lineno, **kwargs):
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(lineno, **kwargs)
        return instrs

    def _get_cfg_slice(self, source, lineno):
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(lineno)
        slice_cfg = slicemethod._generate_cfg_slice(instrs)
        return slice_cfg

    def _get_slice(self, source, lineno):
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(lineno)
        return slicemethod.get_slice(instrs)['cfg']

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

    def assertBlockPredecessorsEqual(self, block, predecessors):
        actual = set(block.predecessors.keys())
        if predecessors is None:
            self.assertFalse(actual)
        else:
            self.assertEqual(actual, set(predecessors))

    def assertBlockEqual(self, block, linenos=None, predecessors=None, successors=None):
        self.assertBlockInstrsEqual(block, linenos)
        self.assertBlockPredecessorsEqual(block, predecessors)
        self.assertBlockSuccessorsEqual(block, successors)


# Tests Slice generate CFG related helper functions.
class TestSliceGenerateCFGFuncs(TestSlice):

    def _get_source(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = ("testing\\n"\n'         # line 2
                  '     "testing2\\n"\n'            # line 3
                  '            "testing3")\n'       # line 4
                  '    z = (y\n'                    # line 5
                  '         + y)\n'                 # line 6
                  '    if (z\n'                     # line 7
                  '     < 7 or len(x) < 2):\n'      # line 8
                  '        temp = 5\n'              # line 9
                  '        return z\n'              # line 10
                  '    return x\n')                 # line 11
        return source

    def test_get_linenos_in_func(self):
        source = self._get_source()
        slicemethod = self._get_slice_class(source)
        self.assertEqual(slicemethod.linenos, [1, 2, 5, 6, 7, 8, 9, 10, 11])

    def test_get_variables_in_func(self):
        source = self._get_source()
        slicemethod = self._get_slice_class(source)
        self.assertEqual(slicemethod.variables, set(['x', 'y', 'z', 'temp']))

    def test_get_map_control_linenos_in_func(self):
        source = self._get_source()
        slicemethod = self._get_slice_class(source)
        self.assertEqual(slicemethod.controls, {7: set([9, 10])})

    def test_get_instructions_in_slice(self):
        source = self._get_source()
        instrs = self._get_instrs_slice(source, 11)
        self.assertEqual(instrs, set([2, 3, 4, 11]))

        instrs = self._get_instrs_slice(source, 10)
        self.assertEqual(instrs, set([1, 2, 3, 4, 5, 6, 7, 8, 10]))

        instrs = self._get_instrs_slice(source, 9)
        self.assertEqual(instrs, set([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_get_instructions_in_slice__include_control(self):
        source = self._get_source()
        instrs = self._get_instrs_slice(source, 11, include_control=False)
        self.assertEqual(instrs, set([2, 3, 4, 11]))

        instrs = self._get_instrs_slice(source, 10, include_control=False)
        self.assertEqual(instrs, set([1, 2, 3, 4, 5, 6, 7, 8, 10]))

        instrs = self._get_instrs_slice(source, 9, include_control=False)
        self.assertEqual(instrs, set([9]))

    def test_get_instructions_in_slice__exclude_vars(self):
        source = self._get_source()

        # Line 11.
        instrs = self._get_instrs_slice(source, 11, exclude_vars=['x'])
        self.assertEqual(instrs, set([11]))

        # Line 10.
        instrs = self._get_instrs_slice(source, 10, exclude_vars=['x'])
        self.assertEqual(instrs, set([1, 5, 6, 7, 8, 10]))

        instrs = self._get_instrs_slice(source, 10, exclude_vars=['y'])
        self.assertEqual(instrs, set([2, 3, 4, 5, 6, 7, 8, 10]))

        instrs = self._get_instrs_slice(source, 10, exclude_vars=['z'])
        self.assertEqual(instrs, set([2, 3, 4, 7, 8, 10]))

        # Line 11.
        instrs = self._get_instrs_slice(source, 9, exclude_vars=['x'])
        self.assertEqual(instrs, set([1, 5, 6, 7, 8, 9]))

        instrs = self._get_instrs_slice(source, 9, exclude_vars=['z'])
        self.assertEqual(instrs, set([2, 3, 4, 7, 8, 9]))


# Tests Slice condense algorithm related helper functions.
class TestSliceCondenseFuncs(TestSlice):

    def _get_block(self, predecessor=None, successor=None, instructions=None):
        block = Block()
        if predecessor:
            block.add_predecessor(predecessor)
        if successor:
            block.add_successor(successor)
        if instructions:
            for instruction in instructions:
                block.add_instruction(instruction)
        return block

    def test_condense_cfg_fold_redundant_branch__identical(self):
        start_block = FunctionBlock('funcA')
        exit_block = self._get_block()

        successor_block_1 = self._get_block(start_block, exit_block)
        successor_block_2 = self._get_block(start_block, exit_block)
        successor_block_3 = self._get_block(start_block, exit_block)

        self.assertFalse(start_block.predecessors)
        self.assertEqual(len(start_block.successors), 3)
        self.assertEqual(len(exit_block.predecessors), 3)
        self.assertFalse(exit_block.successors)

        config = parse_json()
        slicemethod = Slice(start_block, config)
        slicemethod._condense_cfg_fold_redundant_branch(start_block)

        # Check for change after calling function.
        self.assertFalse(start_block.predecessors)
        self.assertEqual(len(start_block.successors), 1)
        self.assertEqual(len(exit_block.predecessors), 1)
        self.assertFalse(exit_block.successors)

        self.assertTrue(successor_block_1.label in start_block.successors)
        self.assertTrue(successor_block_1.label in exit_block.predecessors)

        self.assertEqual(len(successor_block_1.successors), 1)
        self.assertEqual(len(successor_block_1.predecessors), 1)
        self.assertFalse(successor_block_2.predecessors)
        self.assertFalse(successor_block_2.successors)
        self.assertFalse(successor_block_3.predecessors)
        self.assertFalse(successor_block_3.successors)

    def test_condense_cfg_fold_redundant_branch__non_identical(self):
        instructions = [Instruction(lineno=1)]
        start_block = FunctionBlock('funcA')
        exit_block = self._get_block()

        successor_block_1 = self._get_block(start_block, exit_block)
        successor_block_2 = self._get_block(start_block, exit_block)
        successor_block_3 = self._get_block(start_block, exit_block, instructions)

        self.assertFalse(start_block.predecessors)
        self.assertEqual(len(start_block.successors), 3)
        self.assertEqual(len(exit_block.predecessors), 3)
        self.assertFalse(exit_block.successors)

        config = parse_json()
        slicemethod = Slice(start_block, config)
        slicemethod._condense_cfg_fold_redundant_branch(start_block)

        # Check for no change after calling function.
        self.assertFalse(start_block.predecessors)
        self.assertEqual(len(start_block.successors), 3)
        self.assertEqual(len(exit_block.predecessors), 3)
        self.assertFalse(exit_block.successors)

    def test_condense_cfg_remove_empty_block(self):
        # On line 218.
        self.skipTest('TODO: Implement (Important)')

    def test_condense_cfg_combine_blocks(self):
        # On line 234.
        self.skipTest('TODO: Implement (Important)')

    def test_condense_cfg_hoist_branch(self):
        # On line 250.
        self.skipTest('TODO: Implement (Important)')


# Tests Slice generating slice and slice map related helper functions.
class TestSliceGenerateSliceFuncs(TestSlice):

    def _get_source(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = ("testing\\n"\n'         # line 2
                  '     "testing2\\n"\n'            # line 3
                  '            "testing3")\n'       # line 4
                  '    z = (y\n'                    # line 5
                  '         + y)\n'                 # line 6
                  '    if (z\n'                     # line 7
                  '     < 7 or len(x) < 2):\n'      # line 8
                  '        temp = 5\n'              # line 9
                  '        return z\n'              # line 10
                  '    return x\n')                 # line 11
        return source

    def test_get_slice__check_cache(self):
        source = self._get_source()
        slicemethod = self._get_slice_class(source)
        instrs = slicemethod._get_instructions_in_slice(10)
        slice_cfg = slicemethod.get_slice(instrs)

        instrs = frozenset(instrs)
        self.assertEqual(set(slicemethod._SLICE_CACHE.keys()), set([instrs]))
        self.assertEqual(slicemethod._SLICE_CACHE[instrs], slice_cfg)

    def test_get_slice_map__check_keys(self):
        source = self._get_source()
        slicemethod = self._get_slice_class(source)
        slice_map = slicemethod.get_slice_map()

        self.assertEqual(set(slice_map.keys()), set([1, 2, 5, 6, 7, 8, 9, 10, 11]))
        self.assertTrue(len(slicemethod._SLICE_CACHE.keys()) > 0)

    def test_get_slice_map__kwargs_check_keys(self):
        source = self._get_source()
        slicemethod = self._get_slice_class(source)
        slice_map = slicemethod.get_slice_map(include_control=False)

        self.assertEqual(set(slice_map.keys()), set([1, 2, 5, 6, 7, 8, 9, 10, 11]))
        self.assertTrue(len(slicemethod._SLICE_CACHE.keys()) > 0)


# Tests Slice comparing slice map related helper functions.
class TestSliceCompareSliceMapFuncs(TestSlice):

    def _get_source(self, var):
        source = ('def funcA():\n'                      # line 1
                  '     a = 5\n'                        # line 2
                  '     hpixels = 5\n'                  # line 3
                  '     wpixels = 10\n'                 # line 4
                  '     for y in range(5):\n'           # line 5
                  '         for x in range(2):\n'       # line 6
                  '             hpixels += 1\n'         # line 7
                  '             new_var = 0\n'          # line 8
                  '         wpixels += 1\n'             # line 9
                  '     print(%s)\n' %var)              # line 10
        return source

    def test_generate_groups(self):
        source = self._get_source('hpixels') # Source not important for tests.
        slicemethod = self._get_slice_class(source)

        linenos = set([10, 8, 7, 5, 1, 2, 4])
        groups = slicemethod._group_suggestions(linenos)
        self.assertEqual(list(groups), [(1, 2), (4, 5), (7, 8)])

        linenos = set([1, 2, 3, 4, 7])
        groups = slicemethod._group_suggestions(linenos)
        self.assertEqual(list(groups), [(1, 4)])

    def test_add_multiline_statements(self):
        self.skipTest('TODO: Implement (Important)')

    def test_split_groups_linenos_indentation(self):
        self.skipTest('TODO: Implement (Important)')

    def test_adjust_multiline_groups(self):
        self.skipTest('TODO: Implement (Important)')

    def test_adjust_control_groups(self):
        self.skipTest('TODO: Implement (Important)')

    def test_trim_unimportant(self):
        self.skipTest('TODO: Implement (Important)')

    def test_split_groups_linenos(self):
        self.skipTest('TODO: Implement (Important)')

    def test_group_suggestions_with_unimportant(self):
        self.skipTest('TODO: Implement (Important)')


# Tests Slice generating suggestions types related helper functions.
class TestSliceGenerateSuggestionTypeFuncs(TestSlice):

    def test_range(self):
        self.skipTest('TODO: Implement')

    def test_get_groups_variables(self):
        self.skipTest('TODO: Implement (Important)')

    def test_compare_slice_maps(self):
        self.skipTest('TODO: Implement')

    def test_get_suggestions_remove_variables(self):
        self.skipTest('TODO: Implement')

    def test_get_suggestions_similar_ref_block(self):
        self.skipTest('TODO: Implement')

    def test_get_suggestions_diff_reference_livevar_block(self):
        self.skipTest('TODO: Implement')

    def test_get_suggestions_diff_reference_livevar_instr(self):
        self.skipTest('TODO: Implement')


# Test Slice generating suggestion related helper functions.
class TestSliceGenerateSuggestionFuncs(TestSlice):

    def test_is_valid_suggestion(self):
        self.skipTest('TODO: Implement (Important)')

    def test_get_referenced_variables(self):
        self.skipTest('TODO: Implement (Important)')

    def test_get_return_variables(self):
        self.skipTest('TODO: Implement (Important)')

    def test_generate_suggestions(self):
        self.skipTest('TODO: Implement')

    def test_add_suggestion_map(self):
        self.skipTest('TODO: Implement')

    def test_add_suggestions(self):
        self.skipTest('TODO: Implement')

    def test_get_suggestions(self):
        self.skipTest('TODO: Implement')

    def test_get_avg_lineno_slice_complexity(self):
        self.skipTest('TODO: Implement')


# Tests conditionals with Slice class.
class TestSliceConditional(TestSlice):

    def _get_source(self, var):
        source = ('def funcA(b):\n'             # line 1
                  '     unused = 1\n'           # line 2
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

    # Test _get_variables_in_func.
    def test_get_variables_in_func(self):
        source = self._get_source('5')
        slicemethod = self._get_slice_class(source)
        variables = slicemethod._get_variables_in_func()
        self.assertEqual(variables, set(['a', 'b', 'c', 'd', 'unused']))

    # Test _get_instructions_in_slice with line 12 as 'a = 5'.
    def test_get_instructions_in_slice_5(self):
        source = self._get_source('5')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([13, 12]))

    # Test _get_instructions_in_slice with line 12 as 'a = a'.
    def test_get_instructions_in_slice_a(self):
        source = self._get_source('a')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([13, 12, 5, 4]))

    # Test _get_instructions_in_slice with line 12 as 'a = b'.
    def test_get_instructions_in_slice_b(self):
        source = self._get_source('b')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([1, 4, 5, 6, 9, 10, 12, 13]))

    # Test _get_instructions_in_slice with line 12 as 'a = c'.
    def test_get_instructions_in_slice_c(self):
        source = self._get_source('c')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([1, 3, 4, 5, 6, 7, 8, 9, 12, 13]))

    # Test _get_instructions_in_slice with line 12 as 'a = d'.
    def test_get_instructions_in_slice_d(self):
        source = self._get_source('d')
        instrs = self._get_instrs_slice(source, 13)
        self.assertEqual(instrs, set([1, 4, 5, 6, 7, 9, 10, 11, 12, 13]))

    # Test _generate_cfg_slice with line 12 as 'a = 5'.
    def test_generate_cfg_slice_5(self):
        source = self._get_source('5')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L5', 'L6'])

        # If conditional.
        block = funcA.successors['L5']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'])

        # After/exit block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['L5', 'L6'], linenos=[12, 13])

    # Test _generate_cfg_slice with line 12 as 'a = a'.
    def test_generate_cfg_slice_a(self):
        source = self._get_source('a')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L5', 'L6'], linenos=[4, 5])

        # If conditional.
        block = funcA.successors['L5']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'])

        # After/exit block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['L5', 'L6'], linenos=[12, 13])

    # Test _generate_cfg_slice with line 12 as 'a = b'.
    def test_generate_cfg_slice_b(self):
        source = self._get_source('b')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L5', 'L6'], linenos=[1, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L5']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'], linenos=[9, 10])

        # After block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['L5', 'L6'], linenos=[12, 13])

    # Test _generate_cfg_slice with line 12 as 'a = c'.
    def test_generate_cfg_slice_c(self):
        source = self._get_source('c')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L5', 'L6'], linenos=[1, 3, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L5']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'], linenos=[7, 8])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'], linenos=[9])

        # After block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['L5', 'L6'], linenos=[12, 13])

    # Test get_slice with line 12 as 'a = d'.
    def test_generate_cfg_slice_d(self):
        source = self._get_source('d')
        funcA = self._get_cfg_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L5', 'L6'], linenos=[1, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L5']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'], linenos=[7])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, predecessors=['funcA'], successors=['L7'], linenos=[9, 10, 11])

        # After block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['L5', 'L6'], linenos=[12, 13])

    # Test get_slice with line 12 as 'a = 5'.
    def test_get_slice_5(self):
        source = self._get_source('5')
        funcA = self._get_slice(source, lineno=13)
        self.assertBlockEqual(funcA, linenos=[12, 13])

    # Test get_slice with line 12 as 'a = a'.
    def test_get_slice_a(self):
        source = self._get_source('a')
        funcA = self._get_slice(source, lineno=13)
        self.assertBlockEqual(funcA, linenos=[4, 5, 12, 13])

    # Test get_slice with line 12 as 'a = b'.
    def test_get_slice_b(self):
        source = self._get_source('b')
        funcA = self._get_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L6', 'L7'], linenos=[1, 4, 5, 6])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, successors=['L7'], predecessors=['funcA'], linenos=[9, 10])

        # After block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['funcA', 'L6'], linenos=[12, 13])

    # Test get_slice with line 12 as 'a = c'.
    def test_get_slice_c(self):
        source = self._get_source('c')
        funcA = self._get_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L5', 'L6'], linenos=[1, 3, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L5']
        self.assertBlockEqual(block, successors=['L7'], predecessors=['funcA'], linenos=[7, 8])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, successors=['L7'], predecessors=['funcA'], linenos=[9])

        # After block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['L5', 'L6'], linenos=[12, 13])

    # Test get_slice with line 12 as 'a = d'.
    def test_get_slice_d(self):
        source = self._get_source('d')
        funcA = self._get_slice(source, lineno=13)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L5', 'L6'], linenos=[1, 4, 5, 6])

        # If conditional.
        block = funcA.successors['L5']
        self.assertBlockEqual(block, successors=['L7'], predecessors=['funcA'], linenos=[7])

        # Else conditional.
        block = funcA.successors['L6']
        self.assertBlockEqual(block, successors=['L7'], predecessors=['funcA'], linenos=[9, 10, 11])

        # After block.
        block = block.successors['L7']
        self.assertBlockEqual(block, predecessors=['L5', 'L6'], linenos=[12, 13])


# Tests loops with Slice class.
class TestSliceForLoops(TestSlice):

    def _get_source(self, var):
        source = ('def funcA():\n'                      # line 1
                  '     a = 5\n'                        # line 2
                  '     hpixels = 5\n'                  # line 3
                  '     wpixels = 10\n'                 # line 4
                  '     for y in range(5):\n'           # line 5
                  '         for x in range(2):\n'       # line 6
                  '             hpixels += 1\n'         # line 7
                  '             new_var = 0\n'          # line 8
                  '         wpixels += 1\n'             # line 9
                  '     print(%s)\n' %var)              # line 10
        return source

    # Test _get_variables_in_func.
    def test_get_variables_in_func(self):
        source = self._get_source('5')
        slicemethod = self._get_slice_class(source)
        variables = slicemethod._get_variables_in_func()
        self.assertEqual(variables, set(['a', 'hpixels', 'wpixels', 'x', 'y', 'new_var']))

    # Test _get_instructions_in_slice with line 10 as 'print(a)'.
    def test_get_instructions_in_slice_a(self):
        source = self._get_source('a')
        instrs = self._get_instrs_slice(source, 10)
        self.assertEqual(instrs, set([2, 10]))

        # Test without including extra control.
        instrs = self._get_instrs_slice(source, 10, include_control=False)
        self.assertEqual(instrs, set([2, 10]))

    # Test _get_instructions_in_slice with line 10 as 'print(wpixels)'.
    def test_get_instructions_in_slice_wpixels(self):
        source = self._get_source('wpixels')
        instrs = self._get_instrs_slice(source, 10)
        self.assertEqual(instrs, set([4, 5, 9, 10]))

        # Test without including extra control.
        instrs = self._get_instrs_slice(source, 10, include_control=False)
        self.assertEqual(instrs, set([4, 5, 9, 10]))

    # Test _get_instructions_in_slice with line 10 as 'print(hpixels)'.
    def test_get_instructions_in_slice_hpixels(self):
        source = self._get_source('hpixels')
        instrs = self._get_instrs_slice(source, 10)
        self.assertEqual(instrs, set([3, 5, 6, 7, 10]))

        # Test without including extra control.
        instrs = self._get_instrs_slice(source, 10, include_control=False)
        self.assertEqual(instrs, set([3, 5, 6, 7, 10]))

        # Test with excluding x.
        instrs = self._get_instrs_slice(source, 10, exclude_vars=['x'])
        self.assertEqual(instrs, set([3, 5, 6, 7, 10]))

    # Test _get_instructions_in_slice with line 8 as 'new_var = 0'.
    def test_get_instructions_in_slice_new_var_line8(self):
        source = self._get_source('"NA"')
        instrs = self._get_instrs_slice(source, 8)
        self.assertEqual(instrs, set([5, 6, 8]))

        # Test without including extra control.
        instrs = self._get_instrs_slice(source, 8, include_control=False)
        self.assertEqual(instrs, set([8]))

    # Test _get_instructions_in_slice with line 10 as 'print(new_var)'.
    def test_get_instructions_in_slice_new_var_line10(self):
        source = self._get_source('new_var')
        instrs = self._get_instrs_slice(source, 10)
        self.assertEqual(instrs, set([5, 6, 8, 10]))

        # Test without including extra control.
        instrs = self._get_instrs_slice(source, 10, include_control=False)
        self.assertEqual(instrs, set([8, 10]))

    # Test get_slice with line 10 as 'print(a)'.
    def test_get_slice_a(self):
        source = self._get_source('a')
        funcA = self._get_cfg_slice(source, lineno=10)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L8'], linenos=[2])

        # Guard block 1.
        guard_block_1 = funcA.successors['L8']
        self.assertBlockEqual(guard_block_1, predecessors=['funcA', 'L11'], successors=['L9', 'L12'])

        # Guard block 2.
        guard_block_2 = guard_block_1.successors['L9']
        self.assertBlockEqual(guard_block_2, predecessors=['L8', 'L10'], successors=['L10', 'L11'])

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockEqual(body_block_2, predecessors=['L9'], successors=['L9'])

        # After block 2.
        after_block_2 = guard_block_2.successors['L11']
        self.assertBlockEqual(after_block_2, predecessors=['L9'], successors=['L8'])

        # After block 1.
        after_block_1 = guard_block_1.successors['L12']
        self.assertBlockEqual(after_block_1, predecessors=['L8'], linenos=[10])

    # Test _generate_cfg_slice with line 9 as 'print(wpixels)'.
    def test_generate_cfg_slice_wpixels(self):
        source = self._get_source('wpixels')
        funcA = self._get_cfg_slice(source, lineno=10)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L8'], linenos=[4])

        # Guard block 1.
        guard_block_1 = funcA.successors['L8']
        self.assertBlockEqual(guard_block_1, predecessors=['funcA', 'L11'], successors=['L9', 'L12'], linenos=[5])

        # Guard block 2.
        guard_block_2 = guard_block_1.successors['L9']
        self.assertBlockEqual(guard_block_2, predecessors=['L8', 'L10'], successors=['L10', 'L11'])

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockEqual(body_block_2, predecessors=['L9'], successors=['L9'])

        # After block 2.
        after_block_2 = guard_block_2.successors['L11']
        self.assertBlockEqual(after_block_2, predecessors=['L9'], successors=['L8'], linenos=[9])

        # After block 1.
        after_block_1 = guard_block_1.successors['L12']
        self.assertBlockEqual(after_block_1, predecessors=['L8'], linenos=[10])

    # Test _generate_cfg_slice with line 10 as 'print(hpixels)'.
    def test_generate_cfg_slice_hpixels(self):
        source = self._get_source('hpixels')
        funcA = self._get_cfg_slice(source, lineno=10)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L8'], linenos=[3])

        # Guard block 1.
        guard_block_1 = funcA.successors['L8']
        self.assertBlockEqual(guard_block_1, predecessors=['funcA', 'L11'], successors=['L9', 'L12'], linenos=[5])

        # Guard block 2.
        guard_block_2 = guard_block_1.successors['L9']
        self.assertBlockEqual(guard_block_2, predecessors=['L8', 'L10'], successors=['L10', 'L11'], linenos=[6])

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockEqual(body_block_2, predecessors=['L9'], successors=['L9'], linenos=[7])

        # After block 1.
        after_block_2 = guard_block_2.successors['L11']
        self.assertBlockEqual(after_block_2, predecessors=['L9'], successors=['L8'])

        # After/exit block.
        after_block = guard_block_1.successors['L12']
        self.assertBlockEqual(after_block, predecessors=['L8'], linenos=[10])

    # Test _generate_cfg_slice with line 10 as 'print(a)'.
    def test_generate_cfg_slice_a(self):
        source = self._get_source('a')
        funcA = self._get_slice(source, lineno=10)
        self.assertBlockEqual(funcA, linenos=[2, 10])

    # Test get_slice with line 10 as 'print(hpixels)'.
    def test_get_slice_wpixels(self):
        source = self._get_source('wpixels')
        funcA = self._get_slice(source, lineno=10)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L8'], linenos=[4])

        # Guard block 1.
        guard_block_1 = funcA.successors['L8']
        self.assertBlockEqual(guard_block_1, predecessors=['funcA', 'L11'], successors=['L11', 'L12'], linenos=[5])

        # Body block 1.
        body_block_1 = guard_block_1.successors['L11']
        self.assertBlockEqual(body_block_1, predecessors=['L8'], successors=['L8'], linenos=[9])

        # After block 1.
        after_block_1 = guard_block_1.successors['L12']
        self.assertBlockEqual(after_block_1, predecessors=['L8'], linenos=[10])

    # Test get_slice with line 10 as 'print(hpixels)'.
    def test_get_slice_hpixels(self):
        source = self._get_source('hpixels')
        funcA = self._get_slice(source, lineno=10)

        # Function block.
        self.assertBlockEqual(funcA, successors=['L8'], linenos=[3])

        # Guard block 1.
        guard_block_1 = funcA.successors['L8']
        self.assertBlockEqual(guard_block_1, predecessors=['funcA', 'L9'], successors=['L9', 'L12'], linenos=[5])

        # Guard block 2.
        guard_block_2 = guard_block_1.successors['L9']
        self.assertBlockEqual(guard_block_2, predecessors=['L8', 'L10'], successors=['L10', 'L8'], linenos=[6])

        # Body block 2.
        body_block_2 = guard_block_2.successors['L10']
        self.assertBlockEqual(body_block_2, predecessors=['L9'], successors=['L9'], linenos=[7])

        # After block 1.
        after_block_1 = guard_block_1.successors['L12']
        self.assertBlockEqual(after_block_1, predecessors=['L8'], linenos=[10])


# Tests conditionals with a return statement with Slice class.
class TestSliceConditionalReturn(TestSlice):

    # TODO: Decide code and make a test suite for code.
    def test_conditional_with_return(self):
        self.skipTest('TODO: Implement (Important)')


# Tests loops with Slice class.
class TestSliceWhileLoops(TestSlice):

    # TODO: Decide code and make a test suite for code.
    def test_while_loop(self):
        self.skipTest('TODO: Implement (Important)')


# Tests a recursive function.
class TestRecursiveFunction(TestSlice):

    # TODO: Decide code and make a test suite for code.
    def test_recursion(self):
        self.skipTest('TODO: Implement (Important)')


# Tests a exception with more than two successors.
class TestExceptionFunction(TestSlice):

    def get_source(self):
        source = ('def funcA(y):\n'                       # line 1
                  '    try:\n'                            # line 2
                  '        return y\n'                    # line 3
                  '    except SyntaxException as e:\n'    # line 4
                  '        return str(e)\n'               # line 5
                  '    except Exception as e:\n'          # line 6
                  '        return str(e)\n')              # line 7
        return source

    # TODO: Decide code and make a test suite for code.
    def test_exception(self):
        self.skipTest('TODO: Implement (Important)')


if __name__ == '__main__':
     unittest.main()
