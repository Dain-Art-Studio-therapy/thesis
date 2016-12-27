# File name: generatecfg.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Date last modified: 12/26/2016
# Python Version: 3.5


from __future__ import print_function
import ast

from src.models.block import Block, BlockList
from src.models.instruction import Instruction


# TODO(ngarg): What should I do with the initial block?
#              How should I deal with combination of scripting vs functional?


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

   # Generates CFG.
   def generate(self, node):
      self._init_variables()
      self.visit(node)
      return self.block_list

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
      self.current_block = Block()
      self.block_list.add(self.current_block)
      self.generic_visit(node)

   # # Interactive(stmt* body)
   # def visit_Interactive(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Interactive')
   #    self.generic_visit(node)

   # # Expression(expr body)
   # def visit_Expression(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Expr')
   #    self.generic_visit(node)

   # # Suite(stmt* body)
   # def visit_Suite(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Suite')
   #    self.generic_visit(self, node)

   # input: FunctionDef(identifier name, arguments args,
   #                    stmt* body, expr* decorator_list)
   # output: None
   def visit_FunctionDef(self, node):
      self.current_block = Block()
      self.block_list.add(self.current_block)
      self.generic_visit(node)

   # # ClassDef(identifier name, expr* bases, stmt* body, expr* decorator_list)
   # def visit_ClassDef(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_ClassDef')
   #    self.generic_visit(node)

   # # Return(expr? value)
   # def visit_Return(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Return')
   #    self.generic_visit(node)

   # # Delete(expr* targets)
   # def visit_Delete(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Delete')
   #    self.generic_visit(node)

   # # Assign(expr* targets, expr value)
   # def visit_Assign(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Assign')
   #    self.generic_visit(node)

   # # AugAssign(expr target, operator op, expr value)
   # def visit_AugAssign(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_AugAssign')
   #    self.generic_visit(node)

   # input: Print(expr? dest, expr* values, bool nl)
   # output: None
   def visit_Print(self, node):
      # Add print to referenced variables for Python 2 & 3 compatability.
      self.current_block.add_reference(node.lineno, variable='print')
      self.generic_visit(node)

   # # For(expr target, expr iter, stmt* body, stmt* orelse)
   # def visit_For(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_For')
   #    self.generic_visit(node)

   # # While(expr test, stmt* body, stmt* orelse)
   # def visit_While(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_While')
   #    self.generic_visit(node)

   # # If(expr test, stmt* body, stmt* orelse)
   # def visit_If(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_If')
   #    self.generic_visit(node)

   # # With(expr context_expr, expr? optional_vars, stmt* body)
   # def visit_With(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_With')
   #    self.generic_visit(node)

   # # Raise(expr? type, expr? inst, expr? tback)
   # def visit_Raise(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Raise')
   #    self.generic_visit(node)

   # # TryExcept(stmt* body, excepthandler* handlers, stmt* orelse)
   # def visit_TryExcept(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_TryExcept')
   #    self.generic_visit(node)

   # # TryFinally(stmt* body, stmt* finalbody)
   # def visit_TryFinally(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_TryFinally')
   #    self.generic_visit(node)

   # # Exec(expr body, expr? globals, expr? locals)
   # def visit_Exec(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Exec')
   #    self.generic_visit(node)

   # # Global(identifier* names)
   # def visit_Global(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Global')
   #    self.generic_visit(node)

   # # Expr(expr value)
   # def visit_Expr(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Expr')
   #    self.generic_visit(node)

   # # ???
   # def visit_Pass(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Pass')
   #    self.generic_visit(node)

   # # ???
   # def visit_Break(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Break')
   #    self.generic_visit(node)

   # # ???
   # def visit_Continue(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Continue')
   #    self.generic_visit(node)

   # # BoolOp(boolop op, expr* values)
   # def visit_BoolOp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_BoolOp')
   #    self.generic_visit(node)

   # # BinOp(expr left, operator op, expr right)
   # def visit_BinOp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_BinOp')
   #    self.generic_visit(node)

   # # UnaryOp(unaryop op, expr operand)
   # def visit_UnaryOp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_UnaryOp')
   #    self.generic_visit(node)

   # # Lambda(arguments args, expr body)
   # def visit_Lambda(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Lambda')
   #    self.generic_visit(node)

   # # IfExp(expr test, expr body, expr orelse)
   # def visit_IfExp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_IfExp')
   #    self.generic_visit(node)

   # # Dict(expr* keys, expr* values)
   # def visit_Dict(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Dict')
   #    self.generic_visit(node)

   # # Set(expr* elts)
   # def visit_Set(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Set')
   #    self.generic_visit(node)

   # # ListComp(expr elt, comprehension* generators)
   # def visit_ListComp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_ListComp')
   #    self.generic_visit(node)

   # # SetComp(expr elt, comprehension* generators)
   # def visit_SetComp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_SetComp')
   #    self.generic_visit(node)

   # # DictComp(expr key, expr value, comprehension* generators)
   # def visit_DictComp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_DictComp')
   #    self.generic_visit(node)

   # # GeneratorExp(expr elt, comprehension* generators)
   # def visit_GeneratorExp(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_GeneratorExp')
   #    self.generic_visit(node)

   # # Yield(expr? value)
   # def visit_Yield(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Yield')
   #    self.generic_visit(node)

   # # Compare(expr left, cmpop* ops, expr* comparators)
   # def visit_Compare(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Compare')
   #    self.generic_visit(node)

   # # input: Call(expr func, expr* args, keyword* keywords,
   # #             expr? starargs, expr? kwargs)
   # # ouput: None
   # def visit_Call(self, node):
   #    for key, value in vars(node).items():
   #       if key != 'func':
   #          self._visit_item(value)

   # # Repr(expr value)
   # def visit_Repr(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Repr')
   #    self.generic_visit(node)

   # # Num(object n) -- a number as a PyObject.
   # def visit_Num(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Num')
   #    self.generic_visit(node)

   # # Str(string s) -- need to specify raw, unicode, etc?
   # def visit_Str(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Str')
   #    print('line %d: (str) "%s"' %(node.lineno, node.s))
   #    self.generic_visit(node)

   # # Attribute(expr value, identifier attr, expr_context ctx)
   # def visit_Attribute(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Attribute')
   #    self.generic_visit(node)

   # # Subscript(expr value, slice slice, expr_context ctx)
   # def visit_Subscript(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Subscript')
   #    self.generic_visit(node)

   # input: Name(identifier id, expr_context ctx)
   # output: str var
   def visit_Name(self, node):
      action = self._visit_item(node.ctx)
      if action == TypeVariable.LOAD:
         self.current_block.add_reference(node.lineno, variable=node.id)
      if action == TypeVariable.STORE:
         self.current_block.add_definition(node.lineno, variable=node.id)

   # # List(expr* elts, expr_context ctx)
   # def visit_List(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_List')
   #    self.generic_visit(node)

   # # Tuple(expr* elts, expr_context ctx)
   # def visit_Tuple(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Tuple')
   #    self.generic_visit(node)

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
   #    # TODO(ngarg): Implement.
   #    print('visit_Del')
   #    self.generic_visit(node)

   # # ???
   # def visit_AugLoad(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_AugLoad')
   #    self.generic_visit(node)

   # # ???
   # def visit_AugStore(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_AugStore')
   #    self.generic_visit(node)

   # # ???
   # def visit_Param(self, node):
   #    # TODO(ngarg): Implement.
   #    `'visit_Param')
   #    self.generic_visit(node)

   # # Ellipsis
   # def visit_Ellipsis(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Ellipsis')
   #    self.generic_visit(node)

   # # Slice(expr? lower, expr? upper, expr? step)
   # def visit_Slice(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Slice')
   #    self.generic_visit(node)

   # # ExtSlice(slice* dims)
   # def visit_ExtSlice(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_ExtSlice')
   #    self.generic_visit(node)

   # # Index(expr value)
   # def visit_Index(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Index')
   #    self.generic_visit(node)

   # # ???
   # def visit_And(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_And')
   #    self.generic_visit(node)

   # # ???
   # def visit_Or(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Or')
   #    self.generic_visit(node)

   # # ???
   # def visit_Add(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Add')
   #    self.generic_visit(node)

   # # ???
   # def visit_Sub(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Sub')
   #    self.generic_visit(node)

   # # ???
   # def visit_Mult(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Mult')
   #    self.generic_visit(node)

   # # ???
   # def visit_Div(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Div')
   #    self.generic_visit(node)

   # # ???
   # def visit_Mod(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Mod')
   #    self.generic_visit(node)

   # # ???
   # def visit_Pow(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Pow')
   #    self.generic_visit(node)

   # # ???
   # def visit_LShift(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_LShift')
   #    self.generic_visit(node)

   # # ???
   # def visit_RShift(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_RShift')
   #    self.generic_visit(node)

   # # ???
   # def visit_BitOr(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_BitOr')
   #    self.generic_visit(node)

   # # ???
   # def visit_BitXor(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_BitXor')
   #    self.generic_visit(node)

   # # ???
   # def visit_BitAnd(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_BitAnd')
   #    self.generic_visit(node)

   # # ???
   # def visit_FloorDiv(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_FloorDiv')
   #    self.generic_visit(node)

   # # ???
   # def visit_Invert(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Invert')
   #    self.generic_visit(node)

   # # ???
   # def visit_Not(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Not')
   #    self.generic_visit(node)

   # # ???
   # def visit_UAdd(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_UAdd')
   #    self.generic_visit(node)

   # # ???
   # def visit_USub(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_USub')
   #    self.generic_visit(node)

   # # ???
   # def visit_Eq(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Eq')
   #    self.generic_visit(node)

   # # ???
   # def visit_NotEq(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_NotEq')
   #    self.generic_visit(node)

   # # ???
   # def visit_Lt(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Lt')
   #    self.generic_visit(node)

   # # ???
   # def visit_Lte(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Lte')
   #    self.generic_visit(node)

   # # ???
   # def visit_Gt(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Gt')
   #    self.generic_visit(node)

   # # ???
   # def visit_Gte(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Gte')
   #    self.generic_visit(node)

   # # ???
   # def visit_Is(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_Is')
   #    self.generic_visit(node)

   # # ???
   # def visit_IsNot(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_IsNot')
   #    self.generic_visit(node)

   # # ???
   # def visit_In(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_In')
   #    self.generic_visit(node)

   # # ???
   # def visit_NotIn(self, node):
   #    # TODO(ngarg): Implement.
   #    print('visit_NotIn')
   #    self.generic_visit(node)
