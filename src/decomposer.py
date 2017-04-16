# File name: decomposer.py
# Author: Nupur Garg
# Date created: 12/25/2016
# Python Version: 3.5


from __future__ import print_function
import argparse
import ast
import sys

from src.models.error import *
from src.models.slice import Slice
from src.generatecfg import CFGGenerator
from src.parser import parse_json


_LEN_PROGRESS_BAR = 40


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
    parser.add_argument('--noprogress', action='store_true', help='Do not print progress bar')
    args = parser.parse_args()
    return args


# Generates progress bars.
def progress_bar(noprogress, func_num, num_funcs):
    if not noprogress:
        percent = func_num / float(num_funcs)
        arrow = '-' * int(round(percent * _LEN_PROGRESS_BAR)-1) + '>'
        spaces = ' ' * (_LEN_PROGRESS_BAR - len(arrow))

        sys.stdout.write("\rStatus: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()


# Removes progress bar.
def remove_progress_bar(noprogress):
    if not noprogress:
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
    print('\n\nRunning file... {}\n'.format(args.filename))

    # Parse JSON file.
    config = parse_json(args.config)

    # Generate AST.
    node = ast.parse(source)
    print_ast(node, args.debug)

    # Generate CFG.
    generator = CFGGenerator(args.debug)
    cfg = generator.generate(node, source)
    num_funcs = cfg.get_num_funcs()
    progress_bar(args.noprogress, func_num=0, num_funcs=num_funcs)

    # Generates suggestions.
    for func_num, func_block in enumerate(cfg.get_funcs()):
        progress_bar(args.noprogress, func_num=func_num + 1, num_funcs=num_funcs)
        func_slice = Slice(func_block, config, args.slow)
        suggestions.extend(func_slice.get_suggestions())
        total_func_complexity += func_slice.get_lineno_complexity()
    remove_progress_bar(args.noprogress)

    # Print suggestions.
    if suggestions:
        # TODO: REMOVE CONDITION AND \t.
        if not args.noprogress:
            print('Each message below indicates lines of \'{}\' you may be able to '
                  'refactor into new function. The parameters and return values '
                  'provided correspond with the new function. Use your own '
                  'discretion when determining if the decomposition is fit for '
                  'you.'.format(args.filename), end=' ')
            if not args.slow:
                print('For additional suggestions try using the flag --slow.', end=' ')
        for suggestion in suggestions:
            print('\n\n\t{}'.format(suggestion))
    else:
        print('No suggestions detected.', end=' ')
        if not args.slow:
            print('For additional suggestions try using the flag --slow.\n')
        else:
            print('{}'.format(' ' * _LEN_PROGRESS_BAR))

    print('Line number complexity: {0:.2f}\n\n'.format(total_func_complexity))


def main():
    try:
        generate_suggestions()
    except DecomposerError as error:
        print(error.message)


if __name__ == '__main__':
    main()
