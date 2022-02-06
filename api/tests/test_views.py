"""Tests for views of api app"""

from django.test import TestCase, tag
from django.http import HttpRequest

from api.views import get_param_or_zero, get_param_or_max_int
from api.tests.constants import (
    TEST_QUERY_PARAM, DIFFERENT_VALUES, MAX_POSITIVE_INTEGER,
)


@tag('api')
class ViewsTests(TestCase):
    """Tests for views"""

    @classmethod
    def setUpTestData(cls):
        cls.test_request = HttpRequest()

        cls.test_request.query_params = TEST_QUERY_PARAM

    def test_get_param_or_zero(self):
        """Test get_param_or_zero function"""

        for param, expected_value in TEST_QUERY_PARAM.items():
            with self.subTest(f'{param=}'):
                real_value = get_param_or_zero(self.test_request, param)

                self.assertEqual(real_value, expected_value)

        for value in DIFFERENT_VALUES:
            with self.subTest(f'{value=}'):
                real_value_for_incorrect_param = get_param_or_zero(
                    self.test_request, value
                )
                real_value_for_incorrect_request = get_param_or_zero(
                    value, 'param'
                )

                self.assertEqual(real_value_for_incorrect_param, '0')
                self.assertEqual(real_value_for_incorrect_request, '0')

    def test_get_param_or_max_int(self):
        """Test get_param_or_max_int function"""

        for param, expected_value in TEST_QUERY_PARAM.items():
            with self.subTest(f'{param=}'):
                real_value = get_param_or_max_int(self.test_request, param)

                self.assertEqual(real_value, expected_value)

        for value in DIFFERENT_VALUES:
            with self.subTest(f'{value=}'):
                real_value_for_incorrect_param = get_param_or_max_int(
                    self.test_request, value
                )
                real_value_for_incorrect_request = get_param_or_max_int(
                    value, 'param'
                )

                self.assertEqual(
                    real_value_for_incorrect_param, MAX_POSITIVE_INTEGER
                )
                self.assertEqual(
                    real_value_for_incorrect_request, MAX_POSITIVE_INTEGER
                )
