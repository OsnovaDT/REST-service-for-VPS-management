"""Tests for views of api app"""

from django.test import TestCase, tag
from django.http import HttpRequest

from api.views import (
    get_param_or_zero, get_param_or_max_int, get_vps_viewset_query_params,
)
from api.tests.constants import (
    TEST_QUERY_PARAM, DIFFERENT_VALUES, MAX_POSITIVE_INTEGER,
    FULL_TEST_QUERY_PARAMS, QUERY_PARAMS_WITHOUT_STATUS,
    QUERY_PARAMS_WITHOUT_CPU_FROM, QUERY_PARAMS_WITHOUT_CPU_TO,
    QUERY_PARAMS_WITHOUT_RAM_FROM, QUERY_PARAMS_WITHOUT_RAM_TO,
    QUERY_PARAMS_WITHOUT_HDD_FROM, QUERY_PARAMS_WITHOUT_HDD_TO,
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

                self.assertEqual(real_value_for_incorrect_param, 0)
                self.assertEqual(real_value_for_incorrect_request, 0)

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

    def test_get_vps_viewset_query_params(self):
        """Test get_vps_viewset_query_params function"""

        # Test full query param
        for expected_query_param in FULL_TEST_QUERY_PARAMS:
            test_request = HttpRequest()
            test_request.query_params = expected_query_param

            with self.subTest(''):
                real_query_param = get_vps_viewset_query_params(test_request)

                self.assertEqual(real_query_param, expected_query_param)

        # Test query param without status
        expected_query_param_without_status = QUERY_PARAMS_WITHOUT_STATUS.copy()
        expected_query_param_without_status.update({'status': None})

        test_request = HttpRequest()
        test_request.query_params = QUERY_PARAMS_WITHOUT_STATUS
        real_query_param = get_vps_viewset_query_params(test_request)

        self.assertEqual(real_query_param, expected_query_param_without_status)

        # Different request
        for value in DIFFERENT_VALUES:
            with self.subTest(f'{value=}'):
                real_query_param = get_vps_viewset_query_params(value)

                self.assertEqual(real_query_param, None)

        # Test query param without cpu_from
        expected_query_param_without_cpu_from = QUERY_PARAMS_WITHOUT_CPU_FROM.copy()
        expected_query_param_without_cpu_from.update({'cpu_from': 0})

        test_request = HttpRequest()
        test_request.query_params = QUERY_PARAMS_WITHOUT_CPU_FROM
        real_query_param = get_vps_viewset_query_params(test_request)

        self.assertEqual(real_query_param, expected_query_param_without_cpu_from)

        # Test query param without ram_from
        expected_query_param_without_ram_from = QUERY_PARAMS_WITHOUT_RAM_FROM.copy()
        expected_query_param_without_ram_from.update({'ram_from': 0})

        test_request = HttpRequest()
        test_request.query_params = QUERY_PARAMS_WITHOUT_RAM_FROM
        real_query_param = get_vps_viewset_query_params(test_request)

        self.assertEqual(real_query_param, expected_query_param_without_ram_from)

        # Test query param without hdd_from
        expected_query_param_without_hdd_from = QUERY_PARAMS_WITHOUT_HDD_FROM.copy()
        expected_query_param_without_hdd_from.update({'hdd_from': 0})

        test_request = HttpRequest()
        test_request.query_params = QUERY_PARAMS_WITHOUT_HDD_FROM
        real_query_param = get_vps_viewset_query_params(test_request)

        self.assertEqual(real_query_param, expected_query_param_without_hdd_from)

        # Test query param without cpu_to
        expected_query_param_without_cpu_to = QUERY_PARAMS_WITHOUT_CPU_TO.copy()
        expected_query_param_without_cpu_to.update({'cpu_to': MAX_POSITIVE_INTEGER})

        test_request = HttpRequest()
        test_request.query_params = QUERY_PARAMS_WITHOUT_CPU_TO
        real_query_param = get_vps_viewset_query_params(test_request)

        self.assertEqual(real_query_param, expected_query_param_without_cpu_to)

        # Test query param without ram_to
        expected_query_param_without_ram_to = QUERY_PARAMS_WITHOUT_RAM_TO.copy()
        expected_query_param_without_ram_to.update({'ram_to': MAX_POSITIVE_INTEGER})

        test_request = HttpRequest()
        test_request.query_params = QUERY_PARAMS_WITHOUT_RAM_TO
        real_query_param = get_vps_viewset_query_params(test_request)

        self.assertEqual(real_query_param, expected_query_param_without_ram_to)

        # Test query param without hdd_to
        expected_query_param_without_hdd_to = QUERY_PARAMS_WITHOUT_HDD_TO.copy()
        expected_query_param_without_hdd_to.update({'hdd_to': MAX_POSITIVE_INTEGER})

        test_request = HttpRequest()
        test_request.query_params = QUERY_PARAMS_WITHOUT_HDD_TO
        real_query_param = get_vps_viewset_query_params(test_request)

        self.assertEqual(real_query_param, expected_query_param_without_hdd_to)
