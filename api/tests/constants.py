"""Constants for testing"""

TEST_QUERY_PARAM = {}

for i in range(9):
    TEST_QUERY_PARAM[f'cpu_from_{i}'] = str(2 * 10 ** i)
    TEST_QUERY_PARAM[f'ram_from_{i}'] = str(256 * 10 ** i)
    TEST_QUERY_PARAM[f'hdd_from_{i}'] = str(512 * 10 ** i)


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
    'a' * 100_000, 'a' * 100_000_000, 122.12323, test_function,
    [[1, 2, 3, (1, 2)]], None, complex(1, 2), -100, bin(20), hex(100),
    range(100), 'class', 'def', 'int', '\n', '\t', TestClass,
    lambda x: x, int, bool, str, object,
)

MAX_POSITIVE_INTEGER = 2_147_483_647
