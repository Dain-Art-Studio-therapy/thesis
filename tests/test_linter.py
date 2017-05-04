# File name: test_linter.py
# Author: Nupur Garg
# Date created: 5/2/2017
# Python Version: 3.5


import unittest

from src.globals import *
from src.linter import *
from src.models.error import *


class TestLinter(unittest.TestCase):

    def _generate_suggestions(self, source):
        node = ast.parse(source)
        suggestions = get_linter_suggestions(node, source)
        return suggestions

    def test_for__no_suggestions(self):
        source = ('def funcA(listA):\n'
                  '    for x in listA:\n'
                  '        print(x)\n')
        suggestions = self._generate_suggestions(source)
        self.assertFalse(suggestions)

    def test_for__has_suggestions(self):
        source = ('def funcA(listA):\n'
                  '    for x in listA:\n'
                  '        print(x)\n'
                  '    else:\n'
                  '        print("No values")\n')
        suggestions = self._generate_suggestions(source)

        self.assertEqual(set(suggestions.keys()), set([5]))
        self.assertEqual(suggestions[5][0], 'Do not use else with for loops.')

    def test_while__no_suggestions(self):
        source = ('def funcA(maximum):\n'
                  '    while x < range(maximum):\n'
                  '        print(x)\n'
                  '        x += 1\n')
        suggestions = self._generate_suggestions(source)
        self.assertFalse(suggestions)

    def test_while__has_suggestions(self):
        source = ('def funcA(maximum):\n'
                  '    while x < range(maximum):\n'
                  '        print(x)\n'
                  '        x += 1\n'
                  '    else:\n'
                  '        print("No values")\n')
        suggestions = self._generate_suggestions(source)

        self.assertEqual(set(suggestions.keys()), set([6]))
        self.assertEqual(suggestions[6][0], 'Do not use else with while loops.')

    def test_try_except__no_suggestions(self):
        source = ('def funcA(num):\n'
                  '    try:\n'
                  '        int(num)\n'
                  '    except:\n'
                  '        print("EXCEPTION")\n')
        suggestions = self._generate_suggestions(source)
        self.assertFalse(suggestions)

    def test_try_except__has_suggestions(self):
        source = ('def funcA(num):\n'
                  '    try:\n'
                  '        int(num)\n'
                  '    except:\n'
                  '        print("EXCEPTION")\n'
                  '    else:\n'
                  '        print("No values")\n')
        suggestions = self._generate_suggestions(source)

        self.assertEqual(set(suggestions.keys()), set([7]))
        self.assertEqual(suggestions[7][0], 'Do not use else with exceptions.')

    def test_conditional_true_false__no_suggestion(self):
        source = ('def funcA(num):\n'
                  '    result = 0\n'
                  '    if num > 5:\n'
                  '        result += 1\n'
                  '    else:\n'
                  '        result -= 1\n'
                  '    print(result)\n')
        suggestions = self._generate_suggestions(source)
        self.assertFalse(suggestions)

    def test_check_return(self):
        linter = LinterTokenParser(debug=True)
        linter.generate(source='')

        # Check "True" case.
        self.assertTrue(linter._check_return_bool('return True\n'))
        self.assertTrue(linter._check_return_bool('return   True'))
        self.assertTrue(linter._check_return_bool('return\tTrue'))

        # Check "False" case.
        self.assertTrue(linter._check_return_bool('return False '))
        self.assertTrue(linter._check_return_bool('return   False  '))
        self.assertTrue(linter._check_return_bool('return\tFalse  \n'))

        # Check generate case.
        self.assertFalse(linter._check_return_bool('return False or False'))
        self.assertFalse(linter._check_return_bool('return\tfalse'))
        self.assertFalse(linter._check_return_bool('return\tTrue or x > 5'))

    def test_check_if(self):
        linter = LinterTokenParser(debug=True)
        linter.generate(source='')

        self.assertTrue(linter._check_if('\tif   x < 5:\n'))
        self.assertTrue(linter._check_if('\tif   (x  < 5) :\n'))
        self.assertTrue(linter._check_if('\tif   (x  \n'))

        self.assertFalse(linter._check_if('\tif'))
        self.assertFalse(linter._check_if('\tift'))

    def test_conditional_true_false__return_if_else(self):
        source = ('def funcA(num):\n'
                  '    if num > 5:\n'
                  '        return True\n'
                  '    else:\n'
                  '        return False\n')
        suggestions = self._generate_suggestions(source)

        self.assertEqual(set(suggestions.keys()), set([2]))
        message = 'Rewrite conditional as a single line return statement: \'return <conditional>\'.'
        self.assertEqual(suggestions[2][0], message)

    def test_conditional_true_false__return_only_if(self):
        source = ('def funcA(num):\n'
                  '    if(num > 5):\n'
                  '        return   True\n'
                  '    return False\n')
        suggestions = self._generate_suggestions(source)

        self.assertEqual(set(suggestions.keys()), set([2]))
        message = 'Rewrite conditional as a single line return statement: \'return <conditional>\'.'
        self.assertEqual(suggestions[2][0], message)

    def test_conditional_true_false__return_if_if_else(self):
        source = ('def funcA(num):\n'
                  '    if(num > 5):\n'
                  '        return   False\n'
                  '    if num > 5:\n'
                  '        return False\n'
                  '    else:\n'
                  '        return True\n')
        suggestions = self._generate_suggestions(source)

        self.assertEqual(set(suggestions.keys()), set([4]))
        message = 'Rewrite conditional as a single line return statement: \'return <conditional>\'.'
        self.assertEqual(suggestions[4][0], message)

    def test_func_inside_func(self):
        source = ('def funcA(num):\n'
                  '    def funcB(num):\n'
                  '        return False\n'
                  '    return True\n')

        with self.assertRaises(FuncInsideFuncError) as context:
            suggestions = self._generate_suggestions(source)

    def test_over_80_line__has_suggestion(self):
        source = ('def funcA(num):\n'
                  '    # this line is a very long line of comment and it '
                  '      should be condensed into one line of comments\n'
                  '    pass')
        suggestions = self._generate_suggestions(source)

        self.assertEqual(set(suggestions.keys()), set([2]))
        message = 'Line length over 80 characters.'
        self.assertEqual(suggestions[2][0], message)

    def test_over_80_line__has_no_suggestion(self):
        source = ('def funcA(num):\n'
                  '    # this line is medium line of code\n'
                  '    if num > 5:\n'
                  '        return num\n'
                  '    return 0\n')
        suggestions = self._generate_suggestions(source)
        self.assertFalse(suggestions)
