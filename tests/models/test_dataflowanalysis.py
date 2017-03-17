# File name: test_dataflowanalysis.py
# Author: Nupur Garg
# Date created: 2/1/2017
# Python Version: 3.5


import unittest
import ast

from src.globals import *
from src.generatecfg import CFGGenerator
from src.models.block import Block
from src.models.dataflowanalysis import *
from src.models.blockinfo import FunctionBlockInformation, ReachingDefinitions


# Test ReachingDefinitionsAnalysis class.
class TestReachingDefinitionsAnalysis(unittest.TestCase):

    def _generate_cfg(self, source):
        node = ast.parse(source)
        generator = CFGGenerator(False)
        return generator.generate(node, source)

    def setUp(self):
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
        self.cfg = self._generate_cfg(source)
        self.funcA = self.cfg.get_func('funcA')

    def test_abstract(self):
        with self.assertRaises(TypeError) as context:
            IterativeDataflowAnalysis(ReachingDefinitions)
        self.assertIsNotNone(context.exception)

    def test_compute_func_gen(self):
        analysismethod = ReachingDefinitionsAnalysis()
        info = FunctionBlockInformation()
        info.init(self.funcA, ReachingDefinitions)

        func_gen = analysismethod._compute_func_gen(info)
        self.assertEqual(func_gen, {'i': set([('funcA', 2), ('funcA', 3), ('L3', 6), ('L6', 10)]),
                                    'j': set([('funcA', 3), ('L3', 7)]),
                                    'a': set([('funcA', 4), ('L5', 9)])})

    def test_compute_gen_kill_func(self):
        analysismethod = ReachingDefinitionsAnalysis()
        info = FunctionBlockInformation()
        info.init(self.funcA, ReachingDefinitions)

        func_gen = analysismethod._compute_func_gen(info)
        analysismethod._compute_gen_kill(info, func_gen)

        # funcA block.
        cur_block_info = info.get_block_info(self.funcA)
        self.assertEqual(cur_block_info.gen, {'i': set([('funcA', 3)]),
                                              'j': set([('funcA', 3)]),
                                              'a': set([('funcA', 4)])})
        self.assertEqual(cur_block_info.kill, {'i': set([('funcA', 2), ('L3', 6), ('L6', 10)]),
                                               'j': set([('L3', 7)]),
                                               'a': set([('L5', 9)])})

        # L2 block.
        guard_block = self.funcA.successors['L2']
        cur_block_info = info.get_block_info(guard_block)
        self.assertEqual(len(cur_block_info.gen), 0)
        self.assertEqual(len(cur_block_info.kill), 0)

        # L3 block.
        loop_body_start_block = guard_block.successors['L3']
        cur_block_info = info.get_block_info(loop_body_start_block)
        self.assertEqual(cur_block_info.gen, {'i': set([('L3', 6)]),
                                              'j': set([('L3', 7)])})
        self.assertEqual(cur_block_info.kill, {'i': set([('funcA', 2), ('funcA', 3), ('L6', 10)]),
                                               'j': set([('funcA', 3)])})

        # L5 block.
        if_body_block = loop_body_start_block.successors['L5']
        cur_block_info = info.get_block_info(if_body_block)
        self.assertEqual(cur_block_info.gen, {'a': set([('L5', 9)])})
        self.assertEqual(cur_block_info.kill, {'a': set([('funcA', 4)])})

        # L6 block.
        loop_body_end_block = loop_body_start_block.successors['L6']
        cur_block_info = info.get_block_info(loop_body_end_block)
        self.assertEqual(cur_block_info.gen, {'i': set([('L6', 10)])})
        self.assertEqual(cur_block_info.kill, {'i': set([('funcA', 2), ('funcA', 3), ('L3', 6)])})

        # L4 block.
        after_block = guard_block.successors['L4']
        cur_block_info = info.get_block_info(after_block)
        self.assertEqual(len(cur_block_info.gen), 0)
        self.assertEqual(len(cur_block_info.kill), 0)

        # L1 block.
        exit_block = after_block.successors['L1']
        cur_block_info = info.get_block_info(exit_block)
        self.assertEqual(len(cur_block_info.gen), 0)
        self.assertEqual(len(cur_block_info.kill), 0)

    def test_compute_gen_kill_instr(self):
        analysismethod = ReachingDefinitionsAnalysis()
        info = FunctionBlockInformation()
        info.init(self.funcA, ReachingDefinitions)

        func_gen = analysismethod._compute_func_gen(info)
        analysismethod._compute_gen_kill(info, func_gen)

        # Line 2.
        cur_instr_info = info.get_instruction_info(2)
        self.assertEqual(cur_instr_info.gen, {'i': set([('funcA', 2)])})
        self.assertEqual(cur_instr_info.kill, {'i': set([('funcA', 3), ('L3', 6), ('L6', 10)])})

        # Line 3.
        cur_instr_info = info.get_instruction_info(3)
        self.assertEqual(cur_instr_info.gen, {'i': set([('funcA', 3)]),
                                              'j': set([('funcA', 3)])})
        self.assertEqual(cur_instr_info.kill, {'i': set([('funcA', 2), ('L3', 6), ('L6', 10)]),
                                               'j': set([('L3', 7)])})

        # Line 4.
        cur_instr_info = info.get_instruction_info(4)
        self.assertEqual(cur_instr_info.gen, {'a': set([('funcA', 4)])})
        self.assertEqual(cur_instr_info.kill, {'a': set([('L5', 9)])})

        # Line 5.
        cur_instr_info = info.get_instruction_info(5)
        self.assertFalse(cur_instr_info.gen)
        self.assertFalse(cur_instr_info.kill)

        # Line 6.
        cur_instr_info = info.get_instruction_info(6)
        self.assertEqual(cur_instr_info.gen, {'i': set([('L3', 6)])})
        self.assertEqual(cur_instr_info.kill, {'i': set([('funcA', 2), ('funcA', 3), ('L6', 10)])})

        # Line 7.
        cur_instr_info = info.get_instruction_info(7)
        self.assertEqual(cur_instr_info.gen, {'j': set([('L3', 7)])})
        self.assertEqual(cur_instr_info.kill, {'j': set([('funcA', 3)])})

        # Line 9.
        cur_instr_info = info.get_instruction_info(9)
        self.assertEqual(cur_instr_info.gen, {'a': set([('L5', 9)])})
        self.assertEqual(cur_instr_info.kill, {'a': set([('funcA', 4)])})

        # Line 10.
        cur_instr_info = info.get_instruction_info(10)
        self.assertEqual(cur_instr_info.gen, {'i': set([('L6', 10)])})
        self.assertEqual(cur_instr_info.kill, {'i': set([('funcA', 2), ('funcA', 3), ('L3', 6)])})

    def test_compute_info_func(self):
        analysismethod = ReachingDefinitionsAnalysis()
        info = analysismethod.analyze(self.funcA)

        # funcA block.
        cur_block_info = info.get_block_info(self.funcA)
        self.assertEqual(len(cur_block_info.in_node), 0)
        self.assertEqual(cur_block_info.out_node, {'i': set([('funcA', 3)]),
                                                   'j': set([('funcA', 3)]),
                                                   'a': set([('funcA', 4)])})

        # L2 block.
        guard_block = self.funcA.successors['L2']
        cur_block_info = info.get_block_info(guard_block)
        self.assertEqual(cur_block_info.in_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                  'j': set([('funcA', 3), ('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_block_info.out_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                   'j': set([('funcA', 3), ('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})

        # L3 block.
        loop_body_start_block = guard_block.successors['L3']
        cur_block_info = info.get_block_info(loop_body_start_block)
        self.assertEqual(cur_block_info.in_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                  'j': set([('funcA', 3), ('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_block_info.out_node, {'i': set([('L3', 6)]),
                                                   'j': set([('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})

        # L5 block.
        if_body_block = loop_body_start_block.successors['L5']
        cur_block_info = info.get_block_info(if_body_block)
        self.assertEqual(cur_block_info.in_node, {'i': set([('L3', 6)]),
                                                  'j': set([('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_block_info.out_node, {'i': set([('L3', 6)]),
                                                   'j': set([('L3', 7)]),
                                                   'a': set([('L5', 9)])})

        # L6 block.
        loop_body_end_block = loop_body_start_block.successors['L6']
        cur_block_info = info.get_block_info(loop_body_end_block)
        self.assertEqual(cur_block_info.in_node, {'i': set([('L3', 6)]),
                                                  'j': set([('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_block_info.out_node, {'i': set([('L6', 10)]),
                                                   'j': set([('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})

        # L4 block.
        after_block = guard_block.successors['L4']
        cur_block_info = info.get_block_info(after_block)
        self.assertEqual(cur_block_info.in_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                  'j': set([('funcA', 3), ('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_block_info.out_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                   'j': set([('funcA', 3), ('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})

        # L2 block.
        exit_block = after_block.successors['L1']
        cur_block_info = info.get_block_info(exit_block)
        self.assertEqual(cur_block_info.in_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                  'j': set([('funcA', 3), ('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_block_info.out_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                   'j': set([('funcA', 3), ('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})

    def test_compute_info_instr(self):
        analysismethod = ReachingDefinitionsAnalysis()
        info = analysismethod.analyze(self.funcA)

        # Line 2.
        cur_instr_info = info.get_instruction_info(2)
        self.assertEqual(cur_instr_info.in_node, {})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('funcA', 2)])})

        # Line 3.
        cur_instr_info = info.get_instruction_info(3)
        self.assertEqual(cur_instr_info.in_node, {'i': set([('funcA', 2)])})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('funcA', 3)]),
                                                   'j': set([('funcA', 3)])})

        # Line 4.
        cur_instr_info = info.get_instruction_info(4)
        self.assertEqual(cur_instr_info.in_node, {'i': set([('funcA', 3)]),
                                                  'j': set([('funcA', 3)])})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('funcA', 3)]),
                                                   'j': set([('funcA', 3)]),
                                                   'a': set([('funcA', 4)])})

        # Line 5.
        cur_instr_info = info.get_instruction_info(5)
        self.assertEqual(cur_instr_info.in_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                  'j': set([('funcA', 3), ('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                   'j': set([('funcA', 3), ('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})

        # Line 6.
        cur_instr_info = info.get_instruction_info(6)
        self.assertEqual(cur_instr_info.in_node, {'i': set([('funcA', 3), ('L6', 10)]),
                                                  'j': set([('funcA', 3), ('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('L3', 6)]),
                                                   'j': set([('funcA', 3), ('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})
        # Line 7.
        cur_instr_info = info.get_instruction_info(7)
        self.assertEqual(cur_instr_info.in_node, {'i': set([('L3', 6)]),
                                                  'j': set([('funcA', 3), ('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('L3', 6)]),
                                                   'j': set([('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})

        # Line 9.
        cur_instr_info = info.get_instruction_info(9)
        self.assertEqual(cur_instr_info.in_node, {'i': set([('L3', 6)]),
                                                  'j': set([('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('L3', 6)]),
                                                   'j': set([('L3', 7)]),
                                                   'a': set([('L5', 9)])})

        # Line 10.
        cur_instr_info = info.get_instruction_info(10)
        self.assertEqual(cur_instr_info.in_node, {'i': set([('L3', 6)]),
                                                  'j': set([('L3', 7)]),
                                                  'a': set([('funcA', 4), ('L5', 9)])})
        self.assertEqual(cur_instr_info.out_node, {'i': set([('L6', 10)]),
                                                   'j': set([('L3', 7)]),
                                                   'a': set([('funcA', 4), ('L5', 9)])})


if __name__ == '__main__':
     unittest.main()
