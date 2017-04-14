# File name: parser.py
# Author: Nupur Garg
# Date created: 4/13/2017
# Python Version: 3.5


import json

from src.globals import *
from src.models.error import *
from src.models.config import Config


_DEFAULT_JSON_FILE = 'src/config/default.json'


# Parses a JSON file into a Config object.
def parse_json(filename=None):
    filename = filename if filename else _DEFAULT_JSON_FILE
    info = None

    # Open file.
    try:
        data_file = open(filename, 'r')
        obj_json = data_file.read()
        info = json.loads(obj_json)
    except FileNotFoundError as e:
        raise FileNotFoundError(filename)

    # Returns Config object.  
    config = Config()
    config.min_diff_complexity_between_slices = info['generating_suggestions']['min_diff_complexity_between_slices']
    config.max_dist_between_grouped_linenos = info['generating_suggestions']['max_dist_between_grouped_linenos']
    config.max_diff_ref_and_live_var_block = info['generating_suggestions']['max_diff_ref_and_live_var_block']

    config.min_lines_in_suggestion = info['validating_suggestions']['min_lines_in_suggestion']
    config.min_variables_parameter_in_suggestion = info['validating_suggestions']['min_variables_parameter_in_suggestion']
    config.max_variables_parameter_in_suggestion = info['validating_suggestions']['max_variables_parameter_in_suggestion']
    config.max_variables_return_in_suggestion = info['validating_suggestions']['max_variables_return_in_suggestion']
    config.min_lines_func_not_in_suggestion = info['validating_suggestions']['min_lines_func_not_in_suggestion']
    data_file.close()
    return config        