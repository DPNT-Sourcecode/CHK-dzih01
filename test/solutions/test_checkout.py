import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):

    def test_checkout(self):
        assert checkout("AC") == 70


class TestCheckoutEmpty(unittest.TestCase):
    def test_checkout(self):
        assert checkout("") == -1


class TestCheckoutNone(unittest.TestCase):
    def test_checkout(self):
        assert checkout(None) == -1


class TestCheckoutUnknownSKU(unittest.TestCase):
    def test_checkout(self):
        assert checkout("ACBFA") == -1


class TestCheckoutOffer1(unittest.TestCase):
    def test_checkout(self):
        assert checkout("AAA") == 130

if __name__ == '__main__':
    unittest.main()
