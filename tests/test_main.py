"""
Test the main module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from main import is_odd, is_odd_str, is_calvin_henggeler


class Test(TestCase):
    def test_is_odd(self):
        assert not is_odd(0)
        assert is_odd(1)
        assert not is_odd(2)

    def test_is_odd_str(self):
        assert is_odd_str("0") == "0 is even."
        assert is_odd_str("1") == "1 is odd."
        assert is_odd_str("2") == "2 is even."
        assert is_odd_str("-1") == "Please enter a number."
        assert is_odd_str("A") == "Please enter a number."
        assert is_odd_str("") == "Please enter a number."

    def test_is_calvin_henggeler(self):
        assert is_calvin_henggeler("Calvin Henggeler") == "Hello, Calvin!"
        assert is_calvin_henggeler("calvin henggeler") == "Hello, Calvin!"
        assert is_calvin_henggeler("Dr. Wolf Palus") == "You are not Calvin"
        assert is_calvin_henggeler("#1") == "You are not Calvin"
