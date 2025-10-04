import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from revision.hw_functions_utils import get_ticket_price


def test_child_free():
    assert get_ticket_price(4) == 0.0


def test_teen_half_price():
    assert get_ticket_price(10) == 50.0


def test_adult_full_price():
    assert get_ticket_price(30) == 100.0


def test_senior_discount():
    assert get_ticket_price(65) == 70.0
