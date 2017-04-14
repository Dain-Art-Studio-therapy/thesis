# File name: decomposer.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


import argparse
import ast
import sys

from src.globals import *
from src.models.slice import Slice
from src.generatecfg import CFGGenerator
from src.parser import parse_json


# Prints AST node recursively.
def print_node(node, tabs):
    tab_str = '     '

    if not isinstance(node, ast.AST):
        return

    print('%s%s' %(tab_str*tabs, type(node)))
    for key, attr in node.__dict__.items():
        print('%s%s  ~~~  %s' %(tab_str*(tabs+1), key, attr))
        if isinstance(attr, list):
            for item in attr:
                print_node(item, tabs+2)
        else:
            print_node(attr, tabs+2)


# Prints AST structure.
def print_ast(node, debug):
    if debug:
        for child_node in node.__dict__['body']:
            print_node(child_node, tabs=0)
            print('')


# Opens and reads file.
def readfile(filename):
    f = open(filename)
    return f.read()


# Processes commandline arguments.
def process_args():
    parser = argparse.ArgumentParser(description='Code to decompose.')
    parser.add_argument('filename', help='file to parse')
    parser.add_argument('--debug', action='store_true', help='print debug messages')
    parser.add_argument('--config', '-c', help='YAML configuration file')
    args = parser.parse_args()
    return args


def main():
    args = process_args()
    source = readfile(args.filename)
    print('Running file... {}'.format(args.filename))

    # Parse JSON file.
    config = parse_json(args.config)

    # Generate AST.
    node = ast.parse(source)
    print_ast(node, args.config)

    # Generate CFG.
    generator = CFGGenerator(args.debug)
    cfg = generator.generate(node, source)

    # Prints slice calculated on the return statement.
    total_complexity = 0
    total_reduced_compexity = 0
    total_func_complexity = 0

    for func_block in cfg.get_funcs():
        func_slice = Slice(func_block, config)

        # Get complexities.
        func_complexity = func_block.get_cyclomatic_complexity()
        func_reduced_complexity = func_slice.condense_cfg(func_block).get_cyclomatic_complexity()
        suggestion_complexity = func_slice.get_lineno_complexity()

        # Print suggestions
        suggestions = func_slice.get_suggestions()
        if suggestions:
            for suggestion in suggestions:
                print("\t{}".format(suggestion))
        # func_slice.print_live_var_data()

        # Total complexity.
        total_complexity += func_complexity
        total_reduced_compexity += func_reduced_complexity
        total_func_complexity += suggestion_complexity
        # print('\t\t{} - {}  |  {}  {}'.format(func_block.label, func_complexity, func_reduced_complexity, func_complexity))

    print('    TOTAL: {0}  |  {1}  |  {2:.2f}\n'.format(total_complexity, total_reduced_compexity, total_func_complexity))


if __name__ == '__main__':
    main()
