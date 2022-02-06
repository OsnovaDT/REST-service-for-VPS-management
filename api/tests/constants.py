"""Constants for testing api application"""

from random import choice


MAX_POSITIVE_INTEGER = 2_147_483_647

### SIMPLE_QUERY_PARAMS ###

SIMPLE_QUERY_PARAMS = {}

for i in range(9):
    SIMPLE_QUERY_PARAMS[f'cpu_from_{i}'] = 2 * 10 ** i
    SIMPLE_QUERY_PARAMS[f'ram_from_{i}'] = 256 * 10 ** i
    SIMPLE_QUERY_PARAMS[f'hdd_from_{i}'] = 512 * 10 ** i

### DIFFERENT_VALUES ###

class TestClass:
    """Empty class for testing"""


def test_function():
    """Empty function for testing"""


DIFFERENT_VALUES = (
    # Values of str and bytes type
    'zero_cpu_from', 'zero_ram_from', 'zero_hdd_from', '', '!@@#Q@$Q',
    'a' * 100, 'a' * 10_000, '\n', '\t', 'class', 'def', 'int',
    'test'.encode(),

    # Values of int, float and bool types
    0, 100_000, -100, 122.12323, True, False,

    # Data structures
    [1, 2, 3], (1, 2), {'a': 1, 'b': 2}, set([1, 2, 3]), [[1, 2, 3, (1, 2)]],

    # Types
    int, bool, str, object, bytes, bytearray, tuple, list, dict, set, float,

    # Classes and functions
    TestClass, test_function, lambda x: x,

    # Others
    None, complex(1, 2), bin(20), hex(100), range(100),
)

### MULTIPLE_QUERY_PARAMS ###

MULTIPLE_QUERY_PARAMS = []

vps_statuses = ('started', 'expected', 'blocked',)

for degree in range(9):
    multiplier = 10 ** degree

    query_params = {
        'status': choice(vps_statuses),

        'cpu_from': 2 * multiplier,
        'cpu_to': 3 * multiplier,

        'ram_from': 256 * multiplier,
        'ram_to': 512 * multiplier,

        'hdd_from': 512 * multiplier,
        'hdd_to': 1024 * multiplier,
    }

    MULTIPLE_QUERY_PARAMS.append(query_params)

MULTIPLE_QUERY_PARAMS = tuple(MULTIPLE_QUERY_PARAMS)

### NOT_FULL_QUERY_PARAMS ###

full_query_params = {
    'status': 'started',
    'cpu_from': 2,
    'cpu_to': 3,
    'ram_from': 256,
    'ram_to': 512,
    'hdd_from': 512,
    'hdd_to': 1024,
}

query_params_without_status = full_query_params.copy()
query_params_without_status.pop('status')

query_params_without_cpu_from = full_query_params.copy()
query_params_without_cpu_from.pop('cpu_from')

query_params_without_cpu_to = full_query_params.copy()
query_params_without_cpu_to.pop('cpu_to')

query_params_without_ram_from = full_query_params.copy()
query_params_without_ram_from.pop('ram_from')

query_params_without_ram_to = full_query_params.copy()
query_params_without_ram_to.pop('ram_to')

query_params_without_hdd_from = full_query_params.copy()
query_params_without_hdd_from.pop('hdd_from')

query_params_without_hdd_to = full_query_params.copy()
query_params_without_hdd_to.pop('hdd_to')

NOT_FULL_QUERY_PARAMS = {
    'without_status': query_params_without_status,
    'without_cpu_from': query_params_without_cpu_from,
    'without_cpu_to': query_params_without_cpu_to,
    'without_ram_from': query_params_without_ram_from,
    'without_ram_to': query_params_without_ram_to,
    'without_hdd_from': query_params_without_hdd_from,
    'without_hdd_to': query_params_without_hdd_to,
}
