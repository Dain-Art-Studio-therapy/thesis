# File name: test_generatecfg.py
# Author: Nupur Garg
# Date created: 12/26/2016
# Python Version: 3.5


import unittest
import ast

from src.globals import *
from src.models.block import Block
from src.models.instruction import InstructionType
from src.generatecfg import TokenGenerator, CFGGenerator


class TestGenerateTokens(unittest.TestCase):

    def setUp(self):
        Block._label_counter.reset()

    def test_get_blank_lines_spaces(self):
        source = ('string0 = "hi0"\n'                           # line 1
                  '\n'                                          # line 2
                  'def funcA():\n'                              # line 3
                  '    string1 = "hi1"\n'                       # line 4
                  '    \n'                                      # line 5
                  '                                       \n'   # line 6
                  '    string2, string3 = string1, "hello"\n'   # line 7
                  '             \n'                             # line 8
                  '    string4 = string5 = "hi3"\n'             # line 9
                  '\n'                                          # line 10
                  '    print(string1)')                         # line 11
        tokens = TokenGenerator(source)
        self.assertEqual(tokens.blank_lines, set([2, 5, 6, 8, 10]))
        self.assertFalse(tokens.comments)
        self.assertFalse(tokens.multiline)

    def test_get_blank_lines_tabs(self):
        source = ('string0 = "hi0"\n'                           # line 1
                  '\n'                                          # line 2
                  'def funcA():\n'                              # line 3
                  '\tstring1 = "hi1"\n'                         # line 4
                  '\t\n'                                        # line 5
                  '\t\t\t\t\t\t\n'                              # line 6
                  '\tstring2, string3 = string1, "hello"\n'     # line 7
                  '\t\t\t\n'                                    # line 8
                  '\tstring4 = string5 = "hi3"\n'               # line 9
                  '\n'                                          # line 10
                  '\tprint(string1)')                           # line 11
        tokens = TokenGenerator(source)
        self.assertEqual(tokens.blank_lines, set([2, 5, 6, 8, 10]))
        self.assertFalse(tokens.comments)
        self.assertFalse(tokens.multiline)

    def test_comments_single_line(self):
        source = ('string0 = "hi0"\n'                           # line 1
                  '# Function A.\n'                             # line 2
                  'def funcA():\n'                              # line 3
                  '    string1 = "hi1"\n'                       # line 4
                  '    # Initialize string1.\n'                 # line 5
                  '    # Also Initialize string2, string 3.\n'  # line 6
                  '    string2, string3 = string1, "hello"\n'   # line 7
                  '    # Initialize string4, string5.\n'        # line 8
                  '    string4 = string5 = ("hi3")\n'           # line 9
                  '    # Print string1.\n'                      # line 10
                  '    print(string1)')                         # line 11
        tokens = TokenGenerator(source)
        self.assertFalse(tokens.blank_lines)
        self.assertEqual(tokens.comments, set([2, 5, 6, 8, 10]))
        self.assertFalse(tokens.multiline)

    def test_comments_multiline(self):
        source = ('string0 = "hi0"\n'                           # line 1
                  '# Regular comment for fun.\n'                # line 2
                  'def funcA():\n'                              # line 3
                  '    string1 = "hi1"\n'                       # line 4
                  '    """\n'                                   # line 5
                  '    Inside comment block"""\n'               # line 6
                  '    string2, string3 = string1, "hello"\n'   # line 7
                  '    """Single line comment block"""\n'       # line 8
                  '    string4 = string5 = "hi3"\n'             # line 9
                  '    """"""\n'                                # line 10
                  '    Last comment block.\n'                   # line 11
                  '    """\n'                                   # line 12
                  '    print(string1)')                         # line 13
        tokens = TokenGenerator(source)
        self.assertFalse(tokens.blank_lines)
        self.assertEqual(tokens.comments, set([2, 5, 6, 8, 10, 11, 12]))
        self.assertFalse(tokens.multiline)

    def test_multiline_parenthesis(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = ("testing\\n"\n'         # line 2
                  '     "testing2\\n"\n'            # line 3
                  '            "testing3")\n'       # line 4
                  '    z = (y\n'                    # line 5
                  '         + y)\n'                 # line 6
                  '    if (z\n'                     # line 7
                  '     < 7 or len(x) < 2):\n'      # line 8
                  '        return z\n'              # line 9
                  '    return (x +\n'               # line 10
                  '           "test")\n')           # line 11
        tokens = TokenGenerator(source)
        self.assertFalse(tokens.blank_lines)
        self.assertFalse(tokens.comments)

        keys = set([2, 3, 4, 5, 6, 7, 8, 10, 11])
        self.assertEqual(set(tokens.multiline.keys()), keys)

        self.assertEqual(tokens.multiline[2], set([2, 3, 4]))
        self.assertEqual(tokens.multiline[3], set([2, 3, 4]))
        self.assertEqual(tokens.multiline[4], set([2, 3, 4]))

        self.assertEqual(tokens.multiline[5], set([5, 6]))
        self.assertEqual(tokens.multiline[6], set([5, 6]))

        self.assertEqual(tokens.multiline[7], set([7, 8]))
        self.assertEqual(tokens.multiline[8], set([7, 8]))

        self.assertEqual(tokens.multiline[10], set([10, 11]))
        self.assertEqual(tokens.multiline[11], set([10, 11]))

    def test_multiline_slash(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = ("testing\\n" \\\n'      # line 2
                  '     #"testing2 (\\n" \\\n'      # line 3
                  '\n'                              # line 4
                  '            "testing3")\n'       # line 5
                  '    z = y\\\n'                   # line 6
                  '         + y\n'                  # line 7
                  '    if z\\\n'                    # line 8
                  '     < 7 or len(x) < 2:\n'       # line 9
                  '        return z\n'              # line 10
                  '    # testing () \\\n'           # line 11
                  '    return x +\\\n'              # line 12
                  '           "test"\n')            # line 13
        tokens = TokenGenerator(source)
        self.assertEqual(tokens.blank_lines, set([4]))
        self.assertEqual(tokens.comments, set([3, 11]))

        keys = set([2, 3, 4, 5, 6, 7, 8, 9, 12, 13])
        self.assertEqual(set(tokens.multiline.keys()), keys)

        self.assertEqual(tokens.multiline[2], set([2, 3, 4, 5]))
        self.assertEqual(tokens.multiline[3], set([2, 3, 4, 5]))
        self.assertEqual(tokens.multiline[4], set([2, 3, 4, 5]))
        self.assertEqual(tokens.multiline[5], set([2, 3, 4, 5]))

        self.assertEqual(tokens.multiline[6], set([6, 7]))
        self.assertEqual(tokens.multiline[7], set([6, 7]))

        self.assertEqual(tokens.multiline[8], set([8, 9]))
        self.assertEqual(tokens.multiline[9], set([8, 9]))

        self.assertEqual(tokens.multiline[12], set([12, 13]))
        self.assertEqual(tokens.multiline[13], set([12, 13]))


class TestGenerateCFG(unittest.TestCase):

    def setUp(self):
        Block._label_counter.reset()
        self.generator = CFGGenerator(False)

    def assertInstrEqual(self, actual, referenced=None, defined=None,
                         instruction_type=None, control=None, multiline=None):
        self.assertEqual(actual.referenced, set(referenced) if referenced else set())
        self.assertEqual(actual.defined, set(defined) if defined else set())
        self.assertEqual(actual.instruction_type, instruction_type)
        self.assertEqual(actual.control, control)
        self.assertEqual(actual.multiline, set(multiline) if multiline else set())

    def assertBlockSuccessorsEqual(self, block, successors=None):
        actual = set(block.successors.keys())
        if successors is None:
            self.assertFalse(actual)
        else:
            self.assertEqual(actual, set(successors))

    def assertBlockPredecessorsEqual(self, block, predecessors=None):
        actual = set(block.predecessors.keys())
        if predecessors is None:
            self.assertFalse(actual)
        else:
            self.assertEqual(actual, set(predecessors))

    def _generate_cfg(self, source):
        node = ast.parse(source)
        cfg = self.generator.generate(node, source)
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
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(3), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(4), referenced=['x'], instruction_type=InstructionType.RETURN)
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        exit_block = func_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['funcA'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_parameters_definitions(self):
        source = ('def funcA(y):\n'
                  '    x = 5\n'
                  '    return x')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(func_block.get_instruction(2), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['x'], instruction_type=InstructionType.RETURN)
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        exit_block = func_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['funcA'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_assignment_simple(self):
        source = ('string0 = "hi"\n'
                  'def funcA():\n'
                  '    string1 = "hi"\n'
                  '    string2, string3 = string1, "hello"\n'
                  '    string4 = string5 = "hi"\n'
                  '    print(string1)')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(3), defined=['string1'])
        self.assertInstrEqual(func_block.get_instruction(4), referenced=['string1'], defined=['string2', 'string3'])
        self.assertInstrEqual(func_block.get_instruction(5), defined=['string4', 'string5'])
        self.assertInstrEqual(func_block.get_instruction(6), referenced=['print', 'string1'])
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        exit_block = func_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['funcA'])
        self.assertBlockSuccessorsEqual(exit_block)

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
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L2', 'L3'])

        if_block = func_block.successors['L2']
        self.assertInstrEqual(if_block.get_instruction(4), referenced=['print'], control=3)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L3'])

        after_block = func_block.successors['L3']
        self.assertInstrEqual(after_block.get_instruction(5), referenced=['print'])
        self.assertBlockPredecessorsEqual(after_block, ['L2', 'funcA'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L3'])
        self.assertBlockSuccessorsEqual(exit_block)

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
        self.assertBlockSuccessorsEqual(func_block, ['L2', 'L3'])

        if_block_1 = func_block.successors['L2']
        self.assertInstrEqual(if_block_1.get_instruction(4), referenced=['print'], control=3)
        self.assertBlockPredecessorsEqual(if_block_1, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block_1, ['L7'])

        else_block_1 = func_block.successors['L3']
        self.assertInstrEqual(else_block_1.get_instruction(5), referenced=['x'], control=3)
        self.assertBlockPredecessorsEqual(else_block_1, ['funcA'])
        self.assertBlockSuccessorsEqual(else_block_1, ['L4', 'L5'])

        if_block_2 = else_block_1.successors['L4']
        self.assertInstrEqual(if_block_2.get_instruction(6), referenced=['print'], control=5)
        self.assertBlockPredecessorsEqual(if_block_2, ['L3'])
        self.assertBlockSuccessorsEqual(if_block_2, ['L6'])

        else_block_2 = else_block_1.successors['L5']
        self.assertInstrEqual(else_block_2.get_instruction(7), instruction_type=InstructionType.ELSE, control=5)
        self.assertInstrEqual(else_block_2.get_instruction(8), referenced=['print'], control=7)
        self.assertInstrEqual(else_block_2.get_instruction(9), referenced=['print'], control=7)
        self.assertBlockPredecessorsEqual(else_block_2, ['L3'])
        self.assertBlockSuccessorsEqual(else_block_2, ['L6'])

        after_block_2 = if_block_2.successors['L6']
        self.assertFalse(after_block_2._instructions)
        self.assertBlockPredecessorsEqual(after_block_2, ['L4', 'L5'])
        self.assertBlockSuccessorsEqual(after_block_2, ['L7'])

        after_block_1 = if_block_1.successors['L7']
        self.assertFalse(after_block_1._instructions)
        self.assertBlockPredecessorsEqual(after_block_1, ['L2', 'L6'])
        self.assertBlockSuccessorsEqual(after_block_1, ['L1'])

        exit_block = after_block_1.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L7'])
        self.assertBlockSuccessorsEqual(exit_block)

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
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L2'])

        guard_block = func_block.successors['L2']
        self.assertInstrEqual(guard_block.get_instruction(4), referenced=['favs'], defined=['item'])
        self.assertBlockPredecessorsEqual(guard_block, ['funcA', 'L3'])
        self.assertBlockSuccessorsEqual(guard_block, ['L3', 'L4'])

        body_block = guard_block.successors['L3']
        self.assertInstrEqual(body_block.get_instruction(5), referenced=['print', 'item', 'name'], control=4)
        self.assertBlockPredecessorsEqual(body_block, ['L2'])
        self.assertBlockSuccessorsEqual(body_block, ['L2'])

        after_block = guard_block.successors['L4']
        self.assertFalse(after_block._instructions)
        self.assertBlockPredecessorsEqual(after_block, ['L2'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L4'])
        self.assertBlockSuccessorsEqual(exit_block)

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
        self.assertBlockSuccessorsEqual(func_block, ['L2'])

        guard_block_1 = func_block.successors['L2']
        self.assertInstrEqual(guard_block_1.get_instruction(3), referenced=['integers'], defined=['numbers'])
        self.assertBlockPredecessorsEqual(guard_block_1, ['funcA', 'L7'])
        self.assertBlockSuccessorsEqual(guard_block_1, ['L3', 'L4'])

        body_start_1 = guard_block_1.successors['L3']
        self.assertFalse(body_start_1._instructions)
        self.assertBlockPredecessorsEqual(body_start_1, ['L2'])
        self.assertBlockSuccessorsEqual(body_start_1, ['L5'])

        guard_block_2 = body_start_1.successors['L5']
        self.assertInstrEqual(guard_block_2.get_instruction(4), referenced=['numbers'], defined=['integer'], control=3)
        self.assertBlockPredecessorsEqual(guard_block_2, ['L3', 'L6'])
        self.assertBlockSuccessorsEqual(guard_block_2, ['L6', 'L7'])

        body_2 = guard_block_2.successors['L6']
        self.assertInstrEqual(body_2.get_instruction(5), referenced=['integer', 'print'], control=4)
        self.assertBlockPredecessorsEqual(body_2, ['L5'])
        self.assertBlockSuccessorsEqual(body_2, ['L5'])

        body_end_1 = guard_block_1.predecessors['L7']
        self.assertInstrEqual(body_end_1.get_instruction(6), referenced=['print'], control=3)
        self.assertBlockPredecessorsEqual(body_end_1, ['L5'])
        self.assertBlockSuccessorsEqual(body_end_1, ['L2'])

        after_block = guard_block_1.successors['L4']
        self.assertInstrEqual(after_block.get_instruction(7), referenced=['print'])
        self.assertBlockPredecessorsEqual(after_block, ['L2'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L4'])
        self.assertBlockSuccessorsEqual(exit_block)

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
        self.assertBlockSuccessorsEqual(func_block, ['L2'])

        guard_block = func_block.successors['L2']
        self.assertInstrEqual(guard_block.get_instruction(3), referenced=['i'])
        self.assertBlockPredecessorsEqual(guard_block, ['funcA', 'L3'])
        self.assertBlockSuccessorsEqual(guard_block, ['L3', 'L4'])

        body_block = guard_block.successors['L3']
        self.assertInstrEqual(body_block.get_instruction(4), defined=['i'], control=3)
        self.assertBlockPredecessorsEqual(body_block, ['L2'])
        self.assertBlockSuccessorsEqual(body_block, ['L2'])

        after_block = guard_block.successors['L4']
        self.assertInstrEqual(after_block.get_instruction(5), referenced=['print'])
        self.assertBlockPredecessorsEqual(after_block, ['L2'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L4'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_loop_single_list_comprehension(self):
        source = ('def funcA():\n'
                  '    x = [i for i in range(5)]\n'
                  '    print(x)\n')
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(2), referenced=['i', 'range'], defined=['x', 'i'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['x', 'print'])
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        exit_block = func_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['funcA'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_mid_function(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = 5\n'                     # line 2
                  '    return x\n'                  # line 3
                  '    print(x)\n')                 # line 4
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.get_instruction_linenos(), set([1, 2, 3]))
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(func_block.get_instruction(2), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['x'], instruction_type=InstructionType.RETURN)
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L1'])

        exit_block = func_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['funcA'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_if(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = 5\n'                     # line 2
                  '    if y < 4:\n'                 # line 3
                  '        return y\n'              # line 4
                  '    return x\n')                 # line 5
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.get_instruction_linenos(), set([1, 2, 3]))
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(func_block.get_instruction(2), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['y'])
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L2', 'L3'])

        if_block = func_block.successors['L2']
        self.assertInstrEqual(if_block.get_instruction(4), referenced=['y'], instruction_type=InstructionType.RETURN, control=3)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L1'])

        else_block = func_block.successors['L3']
        self.assertInstrEqual(else_block.get_instruction(5), referenced=['x'], instruction_type=InstructionType.RETURN)
        self.assertBlockPredecessorsEqual(else_block, ['funcA'])
        self.assertBlockSuccessorsEqual(else_block, ['L1'])

        exit_block = else_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L2', 'L3'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_if_else(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = 5\n'                     # line 2
                  '    if y < 4:\n'                 # line 3
                  '        return y\n'              # line 4
                  '    else:\n'                     # line 5
                  '        return x\n'              # line 6
                  '    return "BAD"\n')             # line 7
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.get_instruction_linenos(), set([1, 2, 3]))
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(func_block.get_instruction(2), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['y'])
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L2', 'L3'])

        if_block = func_block.successors['L2']
        self.assertInstrEqual(if_block.get_instruction(4), referenced=['y'], instruction_type=InstructionType.RETURN, control=3)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L1'])

        else_block = func_block.successors['L3']
        self.assertInstrEqual(else_block.get_instruction(5), instruction_type=InstructionType.ELSE, control=3)
        self.assertInstrEqual(else_block.get_instruction(6), referenced=['x'], instruction_type=InstructionType.RETURN, control=5)
        self.assertBlockPredecessorsEqual(else_block, ['funcA'])
        self.assertBlockSuccessorsEqual(else_block, ['L1'])

        exit_block = else_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L2', 'L3'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_if_no_return(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = 5\n'                     # line 2
                  '    if y < 4:\n'                 # line 3
                  '        print(y)\n'              # line 4
                  '    else:\n'                     # line 5
                  '        return x\n'              # line 6
                  '    return y\n')                 # line 7
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.get_instruction_linenos(), set([1, 2, 3]))
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(func_block.get_instruction(2), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['y'])
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L2', 'L3'])

        if_block = func_block.successors['L2']
        self.assertInstrEqual(if_block.get_instruction(4), referenced=['y', 'print'], control=3)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L4'])

        else_block = func_block.successors['L3']
        self.assertInstrEqual(else_block.get_instruction(5), instruction_type=InstructionType.ELSE, control=3)
        self.assertInstrEqual(else_block.get_instruction(6), referenced=['x'], instruction_type=InstructionType.RETURN, control=5)
        self.assertBlockPredecessorsEqual(else_block, ['funcA'])
        self.assertBlockSuccessorsEqual(else_block, ['L1'])

        after_block = if_block.successors['L4']
        self.assertInstrEqual(after_block.get_instruction(7), referenced=['y'], instruction_type=InstructionType.RETURN)
        self.assertBlockPredecessorsEqual(after_block, ['L2'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L3', 'L4'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_else_no_return(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = 5\n'                     # line 2
                  '    if y < 4:\n'                 # line 3
                  '        return y\n'              # line 4
                  '    else:\n'                     # line 5
                  '        print(x)\n'              # line 6
                  '    return x\n')                 # line 7
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.get_instruction_linenos(), set([1, 2, 3]))
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(func_block.get_instruction(2), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['y'])
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L2', 'L3'])

        if_block = func_block.successors['L2']
        self.assertInstrEqual(if_block.get_instruction(4), referenced=['y'], instruction_type=InstructionType.RETURN, control=3)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L1'])

        else_block = func_block.successors['L3']
        self.assertInstrEqual(else_block.get_instruction(5), instruction_type=InstructionType.ELSE, control=3)
        self.assertInstrEqual(else_block.get_instruction(6), referenced=['x', 'print'], control=5)
        self.assertBlockPredecessorsEqual(else_block, ['funcA'])
        self.assertBlockSuccessorsEqual(else_block, ['L4'])

        after_block = else_block.successors['L4']
        self.assertInstrEqual(after_block.get_instruction(7), referenced=['x'], instruction_type=InstructionType.RETURN)
        self.assertBlockPredecessorsEqual(after_block, ['L3'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L2', 'L4'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_if_elif_else(self):
        source = ('def funcA(y, z):\n'              # line 1
                  '    x = 5\n'                     # line 2
                  '    if y < 4:\n'                 # line 3
                  '        return y\n'              # line 4
                  '    elif z < 4:\n'               # line 5
                  '        return z\n'              # line 6
                  '    else:\n'                     # line 7
                  '        return x\n'              # line 8
                  '    return "BAD"\n')             # line 9
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.get_instruction_linenos(), set([1, 2, 3]))
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y', 'z'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(func_block.get_instruction(2), defined=['x'])
        self.assertInstrEqual(func_block.get_instruction(3), referenced=['y'])
        self.assertBlockPredecessorsEqual(func_block)
        self.assertBlockSuccessorsEqual(func_block, ['L2', 'L3'])

        if_block = func_block.successors['L2']
        self.assertInstrEqual(if_block.get_instruction(4), referenced=['y'], instruction_type=InstructionType.RETURN, control=3)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L1'])

        else_cond_block = func_block.successors['L3']
        self.assertInstrEqual(else_cond_block.get_instruction(5), referenced=['z'], control=3)
        self.assertBlockPredecessorsEqual(else_cond_block, ['funcA'])
        self.assertBlockSuccessorsEqual(else_cond_block, ['L4', 'L5'])

        elif_block = else_cond_block.successors['L4']
        self.assertInstrEqual(elif_block.get_instruction(6), referenced=['z'], instruction_type=InstructionType.RETURN, control=5)
        self.assertBlockPredecessorsEqual(elif_block, ['L3'])
        self.assertBlockSuccessorsEqual(elif_block, ['L1'])

        else_block = else_cond_block.successors['L5']
        self.assertInstrEqual(else_block.get_instruction(7), instruction_type=InstructionType.ELSE, control=5)
        self.assertInstrEqual(else_block.get_instruction(8), referenced=['x'], instruction_type=InstructionType.RETURN, control=7)
        self.assertBlockPredecessorsEqual(else_block, ['L3'])
        self.assertBlockSuccessorsEqual(else_block, ['L1'])

        exit_block = else_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L2', 'L4', 'L5'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_for_with_return(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    for i in range(5):\n'        # line 2
                  '        y -= 1\n'                # line 3
                  '        return y\n'              # line 4
                  '    print(y)\n')                 # line 5
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertBlockSuccessorsEqual(func_block, ['L2'])

        guard_block = func_block.successors['L2']
        self.assertInstrEqual(guard_block.get_instruction(2), referenced=['range'], defined=['i'])
        self.assertBlockPredecessorsEqual(guard_block, ['funcA'])
        self.assertBlockSuccessorsEqual(guard_block, ['L3', 'L4'])

        body_block = guard_block.successors['L3']
        self.assertInstrEqual(body_block.get_instruction(3), defined=['y'], control=2)
        self.assertInstrEqual(body_block.get_instruction(4), referenced=['y'], instruction_type=InstructionType.RETURN, control=2)
        self.assertBlockPredecessorsEqual(body_block, ['L2'])
        self.assertBlockSuccessorsEqual(body_block, ['L1'])

        after_block = guard_block.successors['L4']
        self.assertInstrEqual(after_block.get_instruction(5), referenced=['y', 'print'])
        self.assertBlockPredecessorsEqual(after_block, ['L2'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L3', 'L4'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_while_with_return(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    while y > 4:\n'              # line 2
                  '        y -= 1\n'                # line 3
                  '        return y\n'              # line 4
                  '    print(y)\n')                 # line 5
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertBlockSuccessorsEqual(func_block, ['L2'])

        guard_block = func_block.successors['L2']
        self.assertInstrEqual(guard_block.get_instruction(2), referenced=['y'])
        self.assertBlockPredecessorsEqual(guard_block, ['funcA'])
        self.assertBlockSuccessorsEqual(guard_block, ['L3', 'L4'])

        body_block = guard_block.successors['L3']
        self.assertInstrEqual(body_block.get_instruction(3), defined=['y'], control=2)
        self.assertInstrEqual(body_block.get_instruction(4), referenced=['y'], instruction_type=InstructionType.RETURN, control=2)
        self.assertBlockPredecessorsEqual(body_block, ['L2'])
        self.assertBlockSuccessorsEqual(body_block, ['L1'])

        after_block = guard_block.successors['L4']
        self.assertInstrEqual(after_block.get_instruction(5), referenced=['y', 'print'])
        self.assertBlockPredecessorsEqual(after_block, ['L2'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L3', 'L4'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_return_while_if_with_return(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    while y > 4:\n'              # line 2
                  '        y -= 1\n'                # line 3
                  '        if y < 4:\n'             # line 4
                  '            return y\n')         # line 5
        cfg = self._generate_cfg(source)
        func_block = cfg.get_func('funcA')

        self.assertEqual(func_block.label, 'funcA')
        self.assertInstrEqual(func_block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertBlockSuccessorsEqual(func_block, ['L2'])

        guard_block = func_block.successors['L2']
        self.assertInstrEqual(guard_block.get_instruction(2), referenced=['y'])
        self.assertBlockPredecessorsEqual(guard_block, ['funcA', 'L6'])
        self.assertBlockSuccessorsEqual(guard_block, ['L3', 'L4'])

        body_block = guard_block.successors['L3']
        self.assertInstrEqual(body_block.get_instruction(3), defined=['y'], control=2)
        self.assertInstrEqual(body_block.get_instruction(4), referenced=['y'], control=2)
        self.assertBlockPredecessorsEqual(body_block, ['L2'])
        self.assertBlockSuccessorsEqual(body_block, ['L5', 'L6'])

        if_block = body_block.successors['L5']
        self.assertInstrEqual(if_block.get_instruction(5), referenced=['y'], instruction_type=InstructionType.RETURN, control=4)
        self.assertBlockPredecessorsEqual(if_block, ['L3'])
        self.assertBlockSuccessorsEqual(if_block, ['L1'])

        after_if_block = body_block.successors['L6']
        self.assertFalse(after_if_block.get_instructions())
        self.assertBlockPredecessorsEqual(after_if_block, ['L3'])
        self.assertBlockSuccessorsEqual(after_if_block, ['L2'])

        after_block = guard_block.successors['L4']
        self.assertFalse(after_if_block.get_instructions())
        self.assertBlockPredecessorsEqual(after_block, ['L2'])
        self.assertBlockSuccessorsEqual(after_block, ['L1'])

        exit_block = after_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L4', 'L5'])
        self.assertBlockSuccessorsEqual(exit_block)

    def test_multiline(self):
        source = ('def funcA(y):\n'                 # line 1
                  '    x = ("testing\\n"\n'         # line 2
                  '     "testing2\\n"\n'            # line 3
                  '            "testing3")\n'       # line 4
                  '    z = (y\n'                    # line 5
                  '         + y)\n'                 # line 6
                  '    if (z\n'                     # line 7
                  '     < 7 or len(x) < 2):\n'      # line 8
                  '        return z\n'              # line 9
                  '    return x\n')                 # line 10
        cfg = self._generate_cfg(source)
        block = cfg.get_func('funcA')

        self.assertInstrEqual(block.get_instruction(1), defined=['y'], instruction_type=InstructionType.FUNCTION_HEADER)
        self.assertInstrEqual(block.get_instruction(2), defined=['x'], multiline=set([2, 3, 4]))
        self.assertInstrEqual(block.get_instruction(5), defined=['z'], referenced=['y'], multiline=set([5, 6]))
        self.assertInstrEqual(block.get_instruction(6), referenced=['y'], multiline=set([5, 6]))
        self.assertInstrEqual(block.get_instruction(7), referenced=['z'], multiline=set([7, 8]))
        self.assertInstrEqual(block.get_instruction(8), referenced=['x', 'len'], multiline=set([7, 8]))
        self.assertBlockPredecessorsEqual(block)
        self.assertBlockSuccessorsEqual(block, ['L2', 'L3'])

        if_block = block.successors['L2']
        self.assertInstrEqual(if_block.get_instruction(9), referenced=['z'], instruction_type=InstructionType.RETURN, control=7)
        self.assertBlockPredecessorsEqual(if_block, ['funcA'])
        self.assertBlockSuccessorsEqual(if_block, ['L1'])

        else_block = block.successors['L3']
        self.assertInstrEqual(else_block.get_instruction(10), referenced=['x'], instruction_type=InstructionType.RETURN)
        self.assertBlockPredecessorsEqual(else_block, ['funcA'])
        self.assertBlockSuccessorsEqual(else_block, ['L1'])

        exit_block = else_block.successors['L1']
        self.assertFalse(exit_block.get_instructions())
        self.assertBlockPredecessorsEqual(exit_block, ['L2', 'L3'])
        self.assertBlockSuccessorsEqual(exit_block)


if __name__ == '__main__':
    unittest.main()
