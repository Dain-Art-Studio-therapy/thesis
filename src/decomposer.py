# File name: decomposer.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


import argparse
import ast
import sys

from src.globals import *
from src.models.error import *
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
    try:
        f = open(filename)
    except IOError as e:
        raise FileNotFoundError(filename)
    return f.read()


# Processes commandline arguments.
def process_args():
    parser = argparse.ArgumentParser(description='Code to decompose.')
    parser.add_argument('filename', help='file to parse')
    parser.add_argument('--config', '-c', help='YAML configuration file')
    parser.add_argument('--slow', action='store_true', help='generate all suggestions')
    parser.add_argument('--debug', action='store_true', help='print debug messages')
    args = parser.parse_args()
    return args

# Generates progress bars.
def progress_bar(func_num, num_funcs, bar_length=40):
    percent = func_num / float(num_funcs)
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rStatus: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

# Removes progress bar.
def remove_progress_bar():
    sys.stdout.write("\r")
    sys.stdout.flush()

# Generates suggestions.
def generate_suggestions():
    total_func_complexity = 0
    suggestions = []
    progress = 0

    # Process arguments.
    args = process_args()
    source = readfile(args.filename)
    print('Running file... {}\n'.format(args.filename))

    # Parse JSON file.
    config = parse_json(args.config)

    # Generate AST.
    node = ast.parse(source)
    print_ast(node, args.debug)

    # Generate CFG.
    generator = CFGGenerator(args.debug)
    cfg = generator.generate(node, source)
    num_funcs = cfg.get_num_funcs()
    progress_bar(func_num=0, num_funcs=num_funcs)

    # Generates suggestions.
    for func_num, func_block in enumerate(cfg.get_funcs()):
        progress_bar(func_num=func_num + 1, num_funcs=num_funcs)
        func_slice = Slice(func_block, config)
        suggestions.extend(func_slice.get_suggestions())
        total_func_complexity += func_slice.get_lineno_complexity()
    remove_progress_bar()

    # Print suggestions.
    if suggestions:
        print('Each message below indicates lines of \'{}\' you may be able to '
              'refactor into new function. The parameters and return values '
              'provided correspond with the new function. Use your own '
              'discretion when determining if the decomposition is fit for '
              'you.'.format(args.filename))
        if not args.slow:
            print('\nFor additional suggestions try using the flag --slow.\n')
        for suggestion in suggestions:
            print('{}'.format(suggestion))

    print('Line number complexity: {0:.2f}\n\n'.format(total_func_complexity))


def main():
    try:
        generate_suggestions()
    except DecomposerError as error:
        print(error.message)


if __name__ == '__main__':
    main()
