"""This file contains different constants containing file paths or keys to
validate"""
import os
# --------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

VALID_KEYS = {'cmd1', 'cmd2', 'value1', 'value2', 'file'}
VALID_VALUES = {'filter', 'map', 'sort', 'unique', 'limit'}

QUERY = {
    'filter': 'filter',
    'map': 'map',
    'unique': 'unique',
    'sort': 'sort',
    'limit': 'limit'
}
