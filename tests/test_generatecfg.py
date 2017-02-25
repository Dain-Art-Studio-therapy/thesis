# File name: test_generatecfg.py
# Author: Nupur Garg
# Date created: 12/26/2016
# Python Version: 3.5


import unittest
import ast

from src.globals import *
from src.models.block import Block
from src.models.instruction import InstructionType
from src.generatecfg import CFGGenerator


class TestGenerateCFG(unittest.TestCase):

    def setUp(self):
        Block._label_counter.reset()
        self.generator = CFGGenerator(False)

    def assertInstrEqual(self, actual, referenced=None, defined=None,
                         instruction_type=None, control=None):
        self.assertEqual(actual.referenced, set(referenced) if referenced else set())
        self.assertEqual(actual.defined, set(defined) if defined else set())
        self.assertEqual(actual.instruction_type, instruction_type)
        self.assertEqual(actual.control, control)

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

    def _generate_cfg(self, source):
        node = ast.parse(source)
        cfg = self.generator.generate(node)
        return cfg

    def test_no_code(self):
        source = ''
        cfg = self._generate_cfg(source)
        self.assertEqual(cfg.get_num_funcs(), 0)

    def test_simple_script(self):
        source = 'string = "hi"'
        cfg = self._generate_cfg(source)
        self.assertEqual(cfg.get_num_funcs(), 0)

    def test_instr_type_return(self):
        source = ('string0 = "hi"\n'
                  'def funcA():\n'
                  '    x = 5\n'
                  '    return x')
        cfg = self._generate_cfg(source)
        block = cfg.get_func('funcA')

        self.assertEqual(block.label, 'funcA')
        self.assertInstrEqual(block.get_instruction(3), defined=['x'])
        self.assertInstrEqual(block.get_instruction(4), referenced=['x'], instruction_type=InstructionType.RETURN)

    def test_parameters_definitions(self):
        self.skipTest('TODO: Add test ensuring function parameters are definitions')

    def test_assignment_simple(self):
        source = ('string0 = "hi"\n'
                  'def funcA():\n'
                  '    string1 = "hi"\n'
                  '    string2, string3 = string1, "hello"\n'
                  '    string4 = string5 = "hi"\n'
                  '    print(string1)')
        cfg = self._generate_cfg(source)
        block = cfg.get_func('funcA')

        self.assertEqual(block.label, 'funcA')
        self.assertInstrEqual(block.get_instruction(3), defined=['string1'])
        self.assertInstrEqual(block.get_instruction(4), referenced=['string1'], defined=['string2', 'string3'])
        self.assertInstrEqual(block.get_instruction(5), defined=['string4', 'string5'])
        self.assertInstrEqual(block.get_instruction(6), referenced=['print', 'string1'])

    def test_conditional_only_if(self):
        source = ('def funcA():\n'
                  '    x = int(input("enter test score:"))\n'
                  '    if x < 70:\n'
                  '        print("You need to retake the class.")\n'
                  '    print("Done")\n')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(2), referenced=['int', 'input'], defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['x'])
        self.assertBlockSuccessorsEqual(func_block, ['L1', 'L2'])

        if_block = func_block.successors['L1']
        self.assertInstrEqual(if_block.get_instruction(4), referenced=['print'], control=3)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L2'])

        exit_block = if_block.successors['L2']
        self.assertInstrEqual(exit_block.get_instruction(5), referenced=['print'])
        self.assertBlockPredecessorsEqual(exit_block, ['L1', 'funcA'])

    def test_conditional_simple_if_elif_else(self):
        source = ('def funcA():\n'
                  '    x = int(input("enter test score:"))\n'
                  '    if x < 70:\n'
                  '        print("You need to retake the class.")\n'
                  '    elif x < 85:\n'
                  '        print("You have room for improvement.")\n'
                  '    else:\n'
                  '        print("Great job!")\n'
                  '        print("Testing multi-line else")\n')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(2), referenced=['int', 'input'], defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['x'])
        self.assertBlockSuccessorsEqual(func_block, ['L1', 'L3'])

        if_block_1 = func_block.successors['L1']
        self.assertInstrEqual(if_block_1.get_instruction(4), referenced=['print'], control=3)
        self.assertBlockPredecessorsEqual(if_block_1, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block_1, ['L2'])

        else_block_1 = func_block.successors['L3']
        self.assertInstrEqual(else_block_1.get_instruction(5), referenced=['x'], control=3)
        self.assertBlockPredecessorsEqual(else_block_1, ['funcA'])
        self.assertBlockSuccessorsEqual(else_block_1, ['L4', 'L6'])

        if_block_2 = else_block_1.successors['L4']
        self.assertInstrEqual(if_block_2.get_instruction(6), referenced=['print'], control=5)
        self.assertBlockPredecessorsEqual(if_block_2, ['L3'])
        self.assertBlockSuccessorsEqual(if_block_2, ['L5'])

        else_block_2 = else_block_1.successors['L6']
        self.assertInstrEqual(else_block_2.get_instruction(7), referenced=['else'], control=5)
        self.assertInstrEqual(else_block_2.get_instruction(8), referenced=['print'], control=7)
        self.assertInstrEqual(else_block_2.get_instruction(9), referenced=['print'], control=7)
        self.assertBlockPredecessorsEqual(else_block_2, ['L3'])
        self.assertBlockSuccessorsEqual(else_block_2, ['L5'])

        exit_block_2 = if_block_2.successors['L5']
        self.assertFalse(exit_block_2._instructions)
        self.assertBlockPredecessorsEqual(exit_block_2, ['L4', 'L6'])
        self.assertBlockSuccessorsEqual(exit_block_2, ['L2'])

        exit_block_1 = if_block_1.successors['L2']
        self.assertFalse(exit_block_1._instructions)
        self.assertBlockPredecessorsEqual(exit_block_1, ['L1', 'L5'])

    def test_loop_single_for(self):
        source = ('def funcA():\n'
                  '    favs = ["berry", "apple"]\n'
                  '    name = "peter"\n'
                  '    for item in favs:\n'
                  '        print("%s likes %s" % (name, item))')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(2), defined=['favs'])
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        guard_block = func_block.successors['L1']
        self.assertInstrEqual(guard_block.get_instruction(4), referenced=['favs'], defined=['item'])
        self.assertBlockPredecessorsEqual(guard_block, ['funcA', 'L2'])
        self.assertBlockSuccessorsEqual(guard_block, ['L2', 'L3'])

        body_block = guard_block.successors['L2']
        self.assertInstrEqual(body_block.get_instruction(5), referenced=['print', 'item', 'name'], control=4)
        self.assertBlockPredecessorsEqual(body_block, ['L1'])
        self.assertBlockSuccessorsEqual(body_block, ['L1'])

        exit_block = guard_block.successors['L3']
        self.assertFalse(exit_block._instructions)
        self.assertEqual(list(exit_block.predecessors), ['L1'])

    def test_loop_nested_for(self):
        source = ('def funcA():\n'
                  '    integers = [[1, 2], [3, 4]]\n'
                  '    for numbers in integers:\n'
                  '        for integer in numbers:\n'
                  '            print("%d " %integer)\n'
                  '        print("argh")\n'
                  '    print("done")\n')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(2), defined=['integers'])
        self.assertBlockPredecessorsEqual(func_block, None)
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        guard_block_1 = func_block.successors['L1']
        self.assertInstrEqual(guard_block_1.get_instruction(3), referenced=['integers'], defined=['numbers'])
        self.assertBlockPredecessorsEqual(guard_block_1, ['funcA', 'L6'])
        self.assertBlockSuccessorsEqual(guard_block_1, ['L2', 'L3'])

        body_start_1 = guard_block_1.successors['L2']
        self.assertFalse(body_start_1._instructions)
        self.assertBlockPredecessorsEqual(body_start_1, ['L1'])
        self.assertBlockSuccessorsEqual(body_start_1, ['L4'])

        guard_block_2 = body_start_1.successors['L4']
        self.assertInstrEqual(guard_block_2.get_instruction(4), referenced=['numbers'], defined=['integer'], control=3)
        self.assertBlockPredecessorsEqual(guard_block_2, ['L2', 'L5'])
        self.assertBlockSuccessorsEqual(guard_block_2, ['L5', 'L6'])

        body_2 = guard_block_2.successors['L5']
        self.assertInstrEqual(body_2.get_instruction(5), referenced=['integer', 'print'], control=4)
        self.assertBlockPredecessorsEqual(body_2, ['L4'])
        self.assertBlockSuccessorsEqual(body_2, ['L4'])

        body_end_1 = guard_block_1.predecessors['L6']
        self.assertInstrEqual(body_end_1.get_instruction(6), referenced=['print'], control=3)
        self.assertBlockPredecessorsEqual(body_end_1, ['L4'])
        self.assertBlockSuccessorsEqual(body_end_1, ['L1'])

        exit_block = guard_block_1.successors['L3']
        self.assertInstrEqual(exit_block.get_instruction(7), referenced=['print'])
        self.assertBlockPredecessorsEqual(exit_block, ['L1'])
        self.assertBlockSuccessorsEqual(exit_block, None)

    def test_loop_single_while(self):
        source = ('def funcA():\n'
                  '    i = 0\n'
                  '    while i < 5:\n'
                  '        i += 1\n'
                  '    print("done")\n')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(2), defined=['i'])
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        guard_block = func_block.successors['L1']
        self.assertInstrEqual(guard_block.get_instruction(3), referenced=['i'])
        self.assertBlockPredecessorsEqual(guard_block, ['funcA', 'L2'])
        self.assertBlockSuccessorsEqual(guard_block, ['L2', 'L3'])

        body_block = guard_block.successors['L2']
        self.assertInstrEqual(body_block.get_instruction(4), defined=['i'], control=3)
        self.assertBlockPredecessorsEqual(body_block, ['L1'])
        self.assertBlockSuccessorsEqual(body_block, ['L1'])

        exit_block = guard_block.successors['L3']
        self.assertInstrEqual(exit_block.get_instruction(5), referenced=['print'])
        self.assertBlockPredecessorsEqual(exit_block, ['L1'])

    def test_loop_single_list_comprehension(self):
        source = ('def funcA():\n'
                  '    x = [i for i in range(5)]\n'
                  '    print(x)\n')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(2), referenced=['i', 'range'], defined=['x', 'i'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['x', 'print'])
        self.assertFalse(func_block.successors)

if __name__ == '__main__':
    unittest.main()
