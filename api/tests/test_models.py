"""Tests for models of api application"""

from django.test import TestCase, tag

from api.models import VPS
from api.tests.constants import VPS_STATUSES_FOR_CHOICES


@tag('api_models')
class ModelsTests(TestCase):
    """Tests for models"""

    @classmethod
    def setUpTestData(cls):
        cls.vps = VPS.objects.create(
            cpu=4, ram=512, hdd=256, status='started'
        )

        cls.uid = VPS._meta.get_field('uid')
        cls.cpu = VPS._meta.get_field('cpu')
        cls.ram = VPS._meta.get_field('ram')
        cls.hdd = VPS._meta.get_field('hdd')
        cls.status = VPS._meta.get_field('status')

    def test_verbose_name(self):
        """Test verbose_name parameter for VPS fields"""

        self.assertEqual(self.uid.verbose_name, 'uid')
        self.assertEqual(self.cpu.verbose_name, 'CPU')
        self.assertEqual(self.ram.verbose_name, 'RAM')
        self.assertEqual(self.hdd.verbose_name, 'HDD')
        self.assertEqual(self.status.verbose_name, 'status')

    def test_primary_key(self):
        """Test primary_key parameter for uid field"""

        self.assertTrue(self.uid.primary_key)

    def test_help_text(self):
        """Test help_text parameter for VPS fields"""

        self.assertEqual(self.cpu.help_text, 'Number of cores')
        self.assertEqual(self.ram.help_text, 'MB')
        self.assertEqual(self.hdd.help_text, 'GB')

    def test_default(self):
        """Test default parameter for VPS fields"""

        self.assertEqual(self.cpu.default, 1)

    def test_db_index(self):
        """Test db_index parameter for VPS fields"""

        self.assertTrue(self.cpu.db_index)
        self.assertTrue(self.status.db_index)

    def test_choices(self):
        """Test choices parameter for VPS fields"""

        self.assertEqual(self.status.choices, VPS_STATUSES_FOR_CHOICES)

    def test_max_length(self):
        """Test max_length parameter for VPS fields"""

        self.assertEqual(self.status.max_length, 10)

    def test_str_method(self):
        """Test __str__ method for VPS model"""

        self.assertEqual(
            str(self.vps),
            str(self.vps.uid) + ' (' + str(self.vps.status) + ')'
        )

    def test_model_verbose_name(self):
        """Test verbose_name parameter of VPS model"""

        self.assertEqual(VPS._meta.verbose_name, 'VPS')

    def test_model_verbose_name_plural(self):
        """Test verbose_name_plural parameter of VPS model"""

        self.assertEqual(VPS._meta.verbose_name_plural, 'VPS')

    def test_model_ordering(self):
        """Test ordering parameter of VPS model"""

        self.assertEqual(VPS._meta.ordering, ('-uid',))
