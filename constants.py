import os
# --------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

VALID_KEYS = {'cmd1', 'cmd2', 'value1', 'value2', 'file'}
VALID_VALUES = {'filter', 'map', 'sort', 'unique', 'limit'}
