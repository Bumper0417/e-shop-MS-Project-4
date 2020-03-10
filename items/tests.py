from django.test import TestCase
from .models import Item

# Create your tests here.


class Itemtests(TestCase):
    """Here we will define the tests that we'll run against our Item Models"""

    def test_str(self):
        test_name = Item(name='An Item')
        self.assertEqual(str(test_name), 'An Item')

    def test_category_choise(self):
        test_name = Item(name='w')
        self.assertEqual(str(test_name), 'w')