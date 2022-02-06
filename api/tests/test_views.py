"""Tests for views of api application"""

from django.test import TestCase, tag
from django.http import HttpRequest

from api.views import (
    get_param_or_zero, get_param_or_max_int, get_vps_query_params,
)
from api.tests.constants import (
    SIMPLE_QUERY_PARAMS, DIFFERENT_VALUES, MAX_POSITIVE_INTEGER,
    MULTIPLE_QUERY_PARAMS, NOT_FULL_QUERY_PARAMS,
)


@tag('api_views')
class ViewsTests(TestCase):
    """Tests for views"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_request = HttpRequest()
        cls.test_request.query_params = SIMPLE_QUERY_PARAMS

    def test_get_param_or_zero(self) -> None:
        """Test get_param_or_zero function"""

        # Test that «try» part work correctly
        for param_name, expected_param in SIMPLE_QUERY_PARAMS.items():
            with self.subTest(param_name):
                real_param = get_param_or_zero(
                    self.test_request, param_name
                )

                self.assertEqual(real_param, expected_param)

        # Test that «except» part work correctly
        for value in DIFFERENT_VALUES:
            with self.subTest(value):
                real_param_for_incorrect_param_name = get_param_or_zero(
                    self.test_request, value
                )
                real_param_for_incorrect_request = get_param_or_zero(
                    value, 'param'
                )

                self.assertEqual(real_param_for_incorrect_param_name, 0)
                self.assertEqual(real_param_for_incorrect_request, 0)

    def test_get_param_or_max_int(self) -> None:
        """Test get_param_or_max_int function"""

        # Test that «try» part work correctly
        for param_name, expected_param in SIMPLE_QUERY_PARAMS.items():
            with self.subTest(param_name):
                real_param = get_param_or_max_int(
                    self.test_request, param_name
                )

                self.assertEqual(real_param, expected_param)

        # Test that «except» part work correctly
        for value in DIFFERENT_VALUES:
            with self.subTest(value):
                real_param_for_incorrect_param_name = get_param_or_max_int(
                    self.test_request, value
                )
                real_param_for_incorrect_request = get_param_or_max_int(
                    value, 'param'
                )

                self.assertEqual(
                    real_param_for_incorrect_param_name, MAX_POSITIVE_INTEGER
                )
                self.assertEqual(
                    real_param_for_incorrect_request, MAX_POSITIVE_INTEGER
                )

    def test_get_vps_query_params(self) -> None:
        """Test get_vps_query_params function"""

        # Test that «try» part work correctly
        for expected_query_params in MULTIPLE_QUERY_PARAMS:
            request = HttpRequest()
            request.query_params = expected_query_params

            real_query_params = get_vps_query_params(request)

            self.assertEqual(real_query_params, expected_query_params)

        # Test that «except» part work correctly
        for value in DIFFERENT_VALUES:
            with self.subTest(value):
                real_query_params = get_vps_query_params(value)

                self.assertEqual(real_query_params, None)

        # Test query params without one param
        for key, query_params in NOT_FULL_QUERY_PARAMS.items():
            request = HttpRequest()
            request.query_params = query_params

            real_query_params = get_vps_query_params(request)

            expected_query_params = query_params.copy()

            match key:
                case 'without_status':
                    expected_query_params.update({'status': None})
                case 'without_cpu_from':
                    expected_query_params.update({'cpu_from': 0})
                case 'without_ram_from':
                    expected_query_params.update({'ram_from': 0})
                case 'without_hdd_from':
                    expected_query_params.update({'hdd_from': 0})
                case 'without_cpu_to':
                    expected_query_params.update(
                        {'cpu_to': MAX_POSITIVE_INTEGER}
                    )
                case 'without_ram_to':
                    expected_query_params.update(
                        {'ram_to': MAX_POSITIVE_INTEGER}
                    )
                case 'without_hdd_to':
                    expected_query_params.update(
                        {'hdd_to': MAX_POSITIVE_INTEGER}
                    )

            self.assertEqual(real_query_params, expected_query_params)
