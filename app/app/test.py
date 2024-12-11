"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """" Test module"""

    def test_add_numbers(self):
        """Test Add numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test Subtract"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
