"""
Sample test file for the calc module
"""
from .calc import add,subtract



from django.test import SimpleTestCase


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding two numbers together"""
        result = add(3, 8)

        self.assertEqual(result, 11)

    def test_subtract(self):
        """Test subtracting two numbers"""
        result = (10 - 5)

        self.assertEqual(result, 5)    