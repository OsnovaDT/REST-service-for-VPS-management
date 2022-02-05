"""Tests for views of api app"""

from django.test import TestCase, tag
from django.http import HttpRequest

from api.views import get_param_or_zero
from api.tests.constants import TEST_QUERY_PARAM, DIFFERENT_VALUES


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

        for param in DIFFERENT_VALUES:
            with self.subTest(f'{param=}'):
                real_value = get_param_or_zero(self.test_request, param)

                self.assertEqual(real_value, '0')
