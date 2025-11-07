import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from revision.hw_functions_utils import get_ticket_price

class TestTicketPrice(unittest.TestCase):

    def test_age_free(self):
        age = 5
        expected_price = 0.0
        self.assertEqual(get_ticket_price(age), expected_price)

    def test_age_50_percent_discount(self):
        age = 15
        expected_price = 50.0
        self.assertEqual(get_ticket_price(age), expected_price)

    def test_age_full_price(self):
        age = 30
        expected_price = 100.0
        self.assertEqual(get_ticket_price(age), expected_price)

    def test_age_30_percent_discount(self):
        age = 70
        expected_price = 70.0
        self.assertEqual(get_ticket_price(age), expected_price)

    def test_boundary_case_6(self):
        self.assertEqual(get_ticket_price(6), 50.0)

    def test_boundary_case_59(self):
        self.assertEqual(get_ticket_price(59), 100.0)

    def test_boundary_case_60(self):
        self.assertEqual(get_ticket_price(60), 70.0)

if __name__ == '__main__':
    unittest.main()