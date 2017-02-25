# File name: generatecfg.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


import ast
import _ast

from src.globals import *
from src.models.block import BlockList, Block, FunctionBlock
from src.models.instruction import Instruction, InstructionType


# Type of the variable.
class TypeVariable(object):
    LOAD = 1
    STORE = 2


# Visitor to generate CFG.
class CFGGenerator(ast.NodeVisitor):
    """
    Generates a CFG from an AST.

    debug: bool
        Whether to print debug messages.
    """

    def __init__(self, debug):
        self.debug = debug
        self._init_variables()

    def _init_variables(self):
        self.block_list = BlockList()
        self.current_block = None
        self.current_control = None

    # Generates CFG.
    def generate(self, node):
        self._init_variables()
        self.visit(node)
        return self.block_list

    # Adds a variable to the current block.
    def _add_variable(self, lineno, variable, action):
        if action == TypeVariable.LOAD:
            self.current_block.add_reference(lineno, variable)
        if action == TypeVariable.STORE:
            self.current_block.add_definition(lineno, variable)
        if self.current_control:
            self.current_block.add_instr_control(lineno, self.current_control)

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

    # input: Module(stmt* body)
    # output: None
    def visit_Module(self, node):
        if 'body' in vars(node):
            for child_node in vars(node)['body']:
                if isinstance(child_node, _ast.FunctionDef):
                    self._visit_item(child_node)

    # # Interactive(stmt* body)
    # def visit_Interactive(self, node):
    #     print('visit_Interactive')
    #     self.generic_visit(node)

    # # Expression(expr body)
    # def visit_Expression(self, node):
    #     print('visit_Expr')
    #     self.generic_visit(node)

    # # Suite(stmt* body)
    # def visit_Suite(self, node):
    #     print('visit_Suite')
    #     self.generic_visit(self, node)

    # input: FunctionDef(identifier name, arguments args,
    #                          stmt* body, expr* decorator_list)
    # output: None
    def visit_FunctionDef(self, node):
        self.current_block = FunctionBlock(node.name)
        self.block_list.add(self.current_block)
        self.generic_visit(node)

    # # ClassDef(identifier name, expr* bases, stmt* body, expr* decorator_list)
    # def visit_ClassDef(self, node):
    #     print('visit_ClassDef')
    #     self.generic_visit(node)

    # Return(expr? value)
    def visit_Return(self, node):
        self.current_block.add_instruction_type(node.lineno, InstructionType.RETURN)
        self.generic_visit(node)

    # # Delete(expr* targets)
    # def visit_Delete(self, node):
    #     print('visit_Delete')
    #     self.generic_visit(node)

    # # Assign(expr* targets, expr value)
    # def visit_Assign(self, node):
    #     print('visit_Assign')
    #     self.generic_visit(node)

    # # AugAssign(expr target, operator op, expr value)
    # def visit_AugAssign(self, node):
    #     print('visit_AugAssign')
    #     self.generic_visit(node)

    # input: Print(expr? dest, expr* values, bool nl)
    # output: None
    def visit_Print(self, node):
        # Add print to referenced variables for Python 2 & 3 compatability.
        self._add_variable(node.lineno, 'print', TypeVariable.LOAD)
        self.generic_visit(node)

    # input: For(expr target, expr iter, stmt* body, stmt* orelse)
    # output: Block
    def visit_For(self, node):
        start_block = self.current_block
        guard_block = Block()
        start_body_block = Block()
        after_block = Block()
        prev_control = self.current_control

        # Add successors/predcessors.
        start_block.add_successor(guard_block)
        guard_block.add_successor(start_body_block)
        guard_block.add_successor(after_block)

        # Add target and iter to current block.
        self.current_block = guard_block
        self._visit_item(node.target)
        self._visit_item(node.iter)
        self.current_control = node.target.lineno

        # Add body to body block.
        self.current_block = start_body_block
        self._visit_item(node.body)
        end_body_block = self.current_block
        end_body_block.add_successor(guard_block)

        # TODO(ngarg): Figure out orelse in For.
        # self.generic_visit(node)

        self.current_control = prev_control
        self.current_block = after_block

    # input: While(expr test, stmt* body, stmt* orelse)
    # output: Block
    def visit_While(self, node):
        start_block = self.current_block
        guard_block = Block()
        start_body_block = Block()
        after_block = Block()
        prev_control = self.current_control

        # Add successors/predcessors.
        start_block.add_successor(guard_block)
        guard_block.add_successor(start_body_block)
        guard_block.add_successor(after_block)

        # Add test to current block.
        self.current_block = guard_block
        self._visit_item(node.test)
        self.current_control = node.test.lineno

        # Add body to body block.
        self.current_block = start_body_block
        self._visit_item(node.body)
        end_body_block = self.current_block
        end_body_block.add_successor(guard_block)

        # TODO(ngarg): Figure out orelse in For.
        # self.generic_visit(node)

        self.current_control = prev_control
        self.current_block = after_block

    # input: If(expr test, stmt* body, stmt* orelse)
    # output: None
    def visit_If(self, node):
        start_block = self.current_block
        start_if_block = Block()
        after_block = Block()
        prev_control = self.current_control

        # Add successors/predecessors.
        start_block.add_successor(start_if_block)

        # Add test to current block.
        self._visit_item(node.test)
        self.current_control = node.test.lineno

        # Add body to if block.
        self.current_block = start_if_block
        self._visit_item(node.body)
        end_if_block = self.current_block
        end_if_block.add_successor(after_block)

        # Add orelse to else block.
        if node.orelse:
            start_else_block = Block()
            start_block.add_successor(start_else_block)
            self.current_block = start_else_block

            # If else block then add instruction 'else' as a placeholder.
            if not isinstance(node.orelse[0], _ast.If):
                lineno = node.orelse[0].lineno - 1
                self._add_variable(lineno, 'else', TypeVariable.LOAD)
                self.current_control = (lineno)

            self._visit_item(node.orelse)
            end_if_block = self.current_block
            end_if_block.add_successor(after_block)
        else:
            start_block.add_successor(after_block)

        self.current_control = prev_control
        self.current_block = after_block

    # # With(expr context_expr, expr? optional_vars, stmt* body)
    # def visit_With(self, node):
    #     print('visit_With')
    #     self.generic_visit(node)

    # # Raise(expr? type, expr? inst, expr? tback)
    # def visit_Raise(self, node):
    #     print('visit_Raise')
    #     self.generic_visit(node)

    # # TryExcept(stmt* body, excepthandler* handlers, stmt* orelse)
    # def visit_TryExcept(self, node):
    #     print('visit_TryExcept')
    #     self.generic_visit(node)

    # # TryFinally(stmt* body, stmt* finalbody)
    # def visit_TryFinally(self, node):
    #     print('visit_TryFinally')
    #     self.generic_visit(node)

    # # Exec(expr body, expr? globals, expr? locals)
    # def visit_Exec(self, node):
    #     print('visit_Exec')
    #     self.generic_visit(node)

    # # Global(identifier* names)
    # def visit_Global(self, node):
    #     print('visit_Global')
    #     self.generic_visit(node)

    # # Expr(expr value)
    # def visit_Expr(self, node):
    #     print('visit_Expr')
    #     self.generic_visit(node)

    # # ???
    # def visit_Pass(self, node):
    #     print('visit_Pass')
    #     self.generic_visit(node)

    # # ???
    # def visit_Break(self, node):
    #     print('visit_Break')
    #     self.generic_visit(node)

    # # ???
    # def visit_Continue(self, node):
    #     print('visit_Continue')
    #     self.generic_visit(node)

    # # BoolOp(boolop op, expr* values)
    # def visit_BoolOp(self, node):
    #     print('visit_BoolOp')
    #     self.generic_visit(node)

    # # BinOp(expr left, operator op, expr right)
    # def visit_BinOp(self, node):
    #     print('visit_BinOp')
    #     self.generic_visit(node)

    # # UnaryOp(unaryop op, expr operand)
    # def visit_UnaryOp(self, node):
    #     print('visit_UnaryOp')
    #     self.generic_visit(node)

    # # Lambda(arguments args, expr body)
    # def visit_Lambda(self, node):
    #     print('visit_Lambda')
    #     self.generic_visit(node)

    # # IfExp(expr test, expr body, expr orelse)
    # def visit_IfExp(self, node):
    #     print('visit_IfExp')
    #     self.generic_visit(node)

    # # Dict(expr* keys, expr* values)
    # def visit_Dict(self, node):
    #     print('visit_Dict')
    #     self.generic_visit(node)

    # # Set(expr* elts)
    # def visit_Set(self, node):
    #     print('visit_Set')
    #     self.generic_visit(node)

    # # ListComp(expr elt, comprehension* generators)
    # def visit_ListComp(self, node):
    #     print('visit_ListComp')
    #     self.generic_visit(node)

    # # SetComp(expr elt, comprehension* generators)
    # def visit_SetComp(self, node):
    #     print('visit_SetComp')
    #     self.generic_visit(node)

    # # DictComp(expr key, expr value, comprehension* generators)
    # def visit_DictComp(self, node):
    #     print('visit_DictComp')
    #     self.generic_visit(node)

    # # GeneratorExp(expr elt, comprehension* generators)
    # def visit_GeneratorExp(self, node):
    #     print('visit_GeneratorExp')
    #     self.generic_visit(node)

    # # Yield(expr? value)
    # def visit_Yield(self, node):
    #     print('visit_Yield')
    #     self.generic_visit(node)

    # # Compare(expr left, cmpop* ops, expr* comparators)
    # def visit_Compare(self, node):
    #     print('visit_Compare')
    #     self.generic_visit(node)

    # # Call(expr func, expr* args, keyword* keywords,
    # #      expr? starargs, expr? kwargs)
    # def visit_Call(self, node):
    #     print('visit_Call')
    #     self.generic_visit(node)

    # # Repr(expr value)
    # def visit_Repr(self, node):
    #     print('visit_Repr')
    #     self.generic_visit(node)

    # # Num(object n) -- a number as a PyObject.
    # def visit_Num(self, node):
    #     print('visit_Num')
    #     self.generic_visit(node)

    # # Str(string s) -- need to specify raw, unicode, etc?
    # def visit_Str(self, node):
    #     print('visit_Str')
    #     print('line %d: (str) "%s"' %(node.lineno, node.s))
    #     self.generic_visit(node)

    # # Attribute(expr value, identifier attr, expr_context ctx)
    # def visit_Attribute(self, node):
    #     print('visit_Attribute')
    #     self.generic_visit(node)

    # # Subscript(expr value, slice slice, expr_context ctx)
    # def visit_Subscript(self, node):
    #     print('visit_Subscript')
    #     self.generic_visit(node)

    # input: Name(identifier id, expr_context ctx)
    # output: str var
    def visit_Name(self, node):
        action = self._visit_item(node.ctx)
        self._add_variable(node.lineno, node.id, action)

    # # List(expr* elts, expr_context ctx)
    # def visit_List(self, node):
    #     print('visit_List')
    #     self.generic_visit(node)

    # # Tuple(expr* elts, expr_context ctx)
    # def visit_Tuple(self, node):
    #     print('visit_Tuple')
    #     self.generic_visit(node)

    # input: Load()
    # output: TypeVariable
    def visit_Load(self, node):
        return TypeVariable.LOAD

    # input: Store()
    # output: TypeVariable
    def visit_Store(self, node):
        return TypeVariable.STORE

    # # ???
    # def visit_Del(self, node):
    #     print('visit_Del')
    #     self.generic_visit(node)

    # # ???
    # def visit_AugLoad(self, node):
    #     print('visit_AugLoad')
    #     self.generic_visit(node)

    # # ???
    # def visit_AugStore(self, node):
    #     print('visit_AugStore')
    #     self.generic_visit(node)

    # Param()
    def visit_Param(self, node):
        return TypeVariable.LOAD

    # # Ellipsis
    # def visit_Ellipsis(self, node):
    #     print('visit_Ellipsis')
    #     self.generic_visit(node)

    # # Slice(expr? lower, expr? upper, expr? step)
    # def visit_Slice(self, node):
    #     print('visit_Slice')
    #     self.generic_visit(node)

    # # ExtSlice(slice* dims)
    # def visit_ExtSlice(self, node):
    #     print('visit_ExtSlice')
    #     self.generic_visit(node)

    # # Index(expr value)
    # def visit_Index(self, node):
    #     print('visit_Index')
    #     self.generic_visit(node)

    # # ???
    # def visit_And(self, node):
    #     print('visit_And')
    #     self.generic_visit(node)

    # # ???
    # def visit_Or(self, node):
    #     print('visit_Or')
    #     self.generic_visit(node)

    # # ???
    # def visit_Add(self, node):
    #     print('visit_Add')
    #     self.generic_visit(node)

    # # ???
    # def visit_Sub(self, node):
    #     print('visit_Sub')
    #     self.generic_visit(node)

    # # ???
    # def visit_Mult(self, node):
    #     print('visit_Mult')
    #     self.generic_visit(node)

    # # ???
    # def visit_Div(self, node):
    #     print('visit_Div')
    #     self.generic_visit(node)

    # # ???
    # def visit_Mod(self, node):
    #     print('visit_Mod')
    #     self.generic_visit(node)

    # # ???
    # def visit_Pow(self, node):
    #     print('visit_Pow')
    #     self.generic_visit(node)

    # # ???
    # def visit_LShift(self, node):
    #     print('visit_LShift')
    #     self.generic_visit(node)

    # # ???
    # def visit_RShift(self, node):
    #     print('visit_RShift')
    #     self.generic_visit(node)

    # # ???
    # def visit_BitOr(self, node):
    #     print('visit_BitOr')
    #     self.generic_visit(node)

    # # ???
    # def visit_BitXor(self, node):
    #     print('visit_BitXor')
    #     self.generic_visit(node)

    # # ???
    # def visit_BitAnd(self, node):
    #     print('visit_BitAnd')
    #     self.generic_visit(node)

    # # ???
    # def visit_FloorDiv(self, node):
    #     print('visit_FloorDiv')
    #     self.generic_visit(node)

    # # ???
    # def visit_Invert(self, node):
    #     print('visit_Invert')
    #     self.generic_visit(node)

    # # ???
    # def visit_Not(self, node):
    #     print('visit_Not')
    #     self.generic_visit(node)

    # # ???
    # def visit_UAdd(self, node):
    #     print('visit_UAdd')
    #     self.generic_visit(node)

    # # ???
    # def visit_USub(self, node):
    #     print('visit_USub')
    #     self.generic_visit(node)

    # # ???
    # def visit_Eq(self, node):
    #     print('visit_Eq')
    #     self.generic_visit(node)

    # # ???
    # def visit_NotEq(self, node):
    #     print('visit_NotEq')
    #     self.generic_visit(node)

    # # ???
    # def visit_Lt(self, node):
    #     print('visit_Lt')
    #     self.generic_visit(node)

    # # ???
    # def visit_Lte(self, node):
    #     print('visit_Lte')
    #     self.generic_visit(node)

    # # ???
    # def visit_Gt(self, node):
    #     print('visit_Gt')
    #     self.generic_visit(node)

    # # ???
    # def visit_Gte(self, node):
    #     print('visit_Gte')
    #     self.generic_visit(node)

    # # ???
    # def visit_Is(self, node):
    #     print('visit_Is')
    #     self.generic_visit(node)

    # # ???
    # def visit_IsNot(self, node):
    #     print('visit_IsNot')
    #     self.generic_visit(node)

    # # ???
    # def visit_In(self, node):
    #     print('visit_In')
    #     self.generic_visit(node)

    # # ???
    # def visit_NotIn(self, node):
    #     print('visit_NotIn')
    #     self.generic_visit(node)
