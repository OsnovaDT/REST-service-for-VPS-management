"""Constants for testing"""

TEST_QUERY_PARAM = {}

for i in range(9):
    TEST_QUERY_PARAM[f'cpu_from_{i}'] = 2 * 10 ** i
    TEST_QUERY_PARAM[f'ram_from_{i}'] = 256 * 10 ** i
    TEST_QUERY_PARAM[f'hdd_from_{i}'] = 512 * 10 ** i


class TestClass:
    """Class for testing"""

    pass


def test_function():
    """Function for testing"""

    pass


DIFFERENT_VALUES = (
    'zero_cpu_from', 'zero_ram_from', 'zero_hdd_from', '',
    0, 100_000, True, False, '!@@#Q@$Q', (1, 2), [1, 2, 3],
    {'a': 1, 'b': 2}, set([1, 2, 3]), 'test'.encode(), 'a' * 100,
    # 'a' * 100_000, 'a' * 100_000_000,
    122.12323, test_function,
    [[1, 2, 3, (1, 2)]], None, complex(1, 2), -100, bin(20), hex(100),
    range(100), 'class', 'def', 'int', '\n', '\t', TestClass,
    lambda x: x, int, bool, str, object,
)

MAX_POSITIVE_INTEGER = 2_147_483_647

from random import choice

VPS_STATUS = ('started', 'expected', 'blocked',)


FULL_TEST_QUERY_PARAMS = []

for i in range(1):
    QUERY_PARAM = {
        'status': choice(VPS_STATUS),
        'cpu_from': 2 * 10 ** i,
        'cpu_to': 3 * 10 ** i,
        'ram_from': 256 * 10 ** i,
        'ram_to': 512 * 10 ** i,
        'hdd_from': 512 * 10 ** i,
        'hdd_to': 1024 * 10 ** i,
    }

    FULL_TEST_QUERY_PARAMS.append(QUERY_PARAM)


QUERY_PARAMS_WITHOUT_STATUS = {
    'cpu_from': 2,
    'cpu_to': 3,
    'ram_from': 256,
    'ram_to': 512,
    'hdd_from': 512,
    'hdd_to': 1024,
}

QUERY_PARAMS_WITHOUT_CPU_FROM = {
    'status': 'started',
    'cpu_to': 3,
    'ram_from': 256,
    'ram_to': 512,
    'hdd_from': 512,
    'hdd_to': 1024,
}

QUERY_PARAMS_WITHOUT_CPU_TO = {
    'status': 'started',
    'cpu_from': 2,
    'ram_from': 256,
    'ram_to': 512,
    'hdd_from': 512,
    'hdd_to': 1024,
}

QUERY_PARAMS_WITHOUT_RAM_FROM = {
    'status': 'started',
    'cpu_from': 2,
    'cpu_to': 3,
    'ram_to': 512,
    'hdd_from': 512,
    'hdd_to': 1024,
}

QUERY_PARAMS_WITHOUT_RAM_TO = {
    'status': 'started',
    'cpu_from': 2,
    'cpu_to': 3,
    'ram_from': 256,
    'hdd_from': 512,
    'hdd_to': 1024,
}

QUERY_PARAMS_WITHOUT_HDD_FROM = {
    'status': 'started',
    'cpu_from': 2,
    'cpu_to': 3,
    'ram_from': 256,
    'ram_to': 512,
    'hdd_to': 1024,
}

QUERY_PARAMS_WITHOUT_HDD_TO = {
    'status': 'started',
    'cpu_from': 2,
    'cpu_to': 3,
    'ram_from': 256,
    'ram_to': 512,
    'hdd_from': 512,
}
