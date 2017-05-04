# File name: linter.py
# Author: Nupur Garg
# Date created: 5/2/2017
# Python Version: 3.5


import ast
import re
import textwrap

from src.globals import *
from src.models.error import *


# Generates suggestions for the linter.
def get_linter_suggestions(node, source, debug=True):
    # Gets LinterTokenParser suggestions.
    parser = LinterTokenParser(source)
    suggestions_map = parser.generate(source)

    # Gets Linter suggestions.
    linter = Linter(debug)
    linter_suggestions_map = linter.generate(node)
    for lineno, suggestions in sorted(linter_suggestions_map.items()):
        if lineno not in suggestions_map:
            suggestions_map[lineno] = []
        suggestions_map[lineno].extend(suggestions)
    return suggestions_map


class LinterTokenParser(object):
    """
    Generates and retains tokens.
    """

    def __init__(self, debug):
        self.debug = debug

    def generate(self, source, line_limit=80):
        self.suggestions = {}
        self.lines = source.splitlines(True)

        # Gets the suggestions.
        self._check_indentation()
        self._check_line_length()
        self._check_conditional_true_false()
        return self.suggestions

    # Adds a suggestion.
    def _add_suggestion(self, lineno, message):
        if lineno not in self.suggestions:
            self.suggestions[lineno] = []
        self.suggestions[lineno].append(message)

    # TODO: Generate on function and program level.
    #       For function do - "Line <start of function>: function name should..."
    #       For program do - "Line 0: program indentation is incorrect"
    # Checks the indentation for a program.
    def _check_indentation(self):
        pass

    # Returns the space at the start of the line.
    def _get_space_start(self, line):
        return re.search(r'(\s*)[^\s]*', line).group(1)

    # Checks if line length is greater than specified.
    def _check_line_length(self, line_limit=80):
        message = 'Line length over {0} characters.'.format(line_limit)
        for lineno, line in enumerate(self.lines, 1):
            if len(line) > line_limit:
                self._add_suggestion(lineno, message)

    # Checks if the return statement is a boolean
    def _check_return_bool(self, line):
        return bool(re.match(r'return\s+(True|False)$', line.strip()))

    # Checks if statement.
    def _check_if(self, line):
        return re.search(r'^if |^if\(', line.strip())

    # Checks else statement.
    def _check_else(self, line):
        return re.search(r'^else\:$', line.strip())

    # TODO: Make it work with multiline statements.
    # TODO: Make sure none of these are comments.
    # Checks conditional that is done as a True/False statement
    def _check_conditional_true_false(self):
        message = 'Rewrite conditional as a single line return statement: \'return <conditional>\'.'
        start_lineno = None
        cond_incr = 0

        for lineno, line in enumerate(self.lines, 1):
            is_bool_return = self._check_return_bool(line)

            if self._check_if(line):
                start_lineno = lineno
                cond_incr = 1
            elif cond_incr == 1 and is_bool_return:
                cond_incr += 1
            elif cond_incr == 2:
                if self._check_else(line):
                    cond_incr += 1
                elif is_bool_return:
                    self._add_suggestion(start_lineno, message)
                else:
                    cond_incr = 0
            elif cond_incr == 3 and is_bool_return:
                self._add_suggestion(start_lineno, message)
                cond_incr = 0
            else:
                cond_incr = 0


class Linter(ast.NodeVisitor):
    """
    Generates Linter messages from an AST.

    debug: bool
        Whether to print debug messages.
    """

    def __init__(self, debug):
        self.debug = debug

    # Generates CFG.
    def generate(self, node):
        self._init_variables()
        self.visit(node)
        return self.suggestions

    # Initializes variables.
    def _init_variables(self):
        self.suggestions = {}
        self.func_name = None

    # Adds suggestions.
    def _add_suggestion(self, lineno, message):
        if lineno not in self.suggestions:
            self.suggestions[lineno] = []
        self.suggestions[lineno].append(message)

    # Visits element within node.
    def _visit_item(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, ast.AST):
                    result = self.visit(item)
                    if isinstance(result, list):
                        items.extend(result)
                    elif result:
                        items.append(result)
            return items
        elif isinstance(value, ast.AST):
            return self.visit(value)

    # input: FunctionDef(identifier name, arguments args,
    #                    stmt* body, expr* decorator_list)
    # output: None
    def visit_FunctionDef(self, node):
        if self.func_name:
            raise FuncInsideFuncError(node.lineno)
        self.func_name = node.name
        self.generic_visit(node)
        self.func_name = None

    # Visits a orelse condition.
    def _visit_orelse(self, orelse, message):
        if orelse:
            lineno = orelse[0].lineno
            self._add_suggestion(lineno, message)

    # input: For(expr target, expr iter, stmt* body, stmt* orelse)
    # output: None
    def visit_For(self, node):
        self._visit_orelse(node.orelse, 'Do not use else with for loops.')

    # input: While(expr test, stmt* body, stmt* orelse)
    # output: None
    def visit_While(self, node):
        self._visit_orelse(node.orelse, 'Do not use else with while loops.')

    # input: TryExcept(stmt* body, excepthandler* handlers, stmt* orelse)
    # output: None
    def visit_TryExcept(self, node):
        self._visit_orelse(node.orelse, 'Do not use else with exceptions.')

    # input: Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
    # output: None
    def visit_Try(self, node):
        self._visit_orelse(node.orelse, 'Do not use else with exceptions.')
