import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):

    def test_checkout(self):
        assert checkout("AC") == 70


class TestCheckoutEmpty(unittest.TestCase):
    def test_checkout(self):
        assert checkout("") == 0


class TestCheckoutNone(unittest.TestCase):
    def test_checkout(self):
        assert checkout(None) == 0


class TestCheckoutOneSKU(unittest.TestCase):

    def test_checkout(self):
        assert checkout("A") == 50


class TestCheckoutUnknownSKU(unittest.TestCase):
    def test_checkout(self):
        assert checkout("ACBXA") == -1


class TestCheckoutOffer1(unittest.TestCase):
    def test_checkout(self):
        assert checkout("AAA") == 130


class TestCheckoutOffer2(unittest.TestCase):
    def test_checkout(self):
        assert checkout("BB") == 45


class TestCheckoutOffer3(unittest.TestCase):
    def test_checkout(self):
        assert checkout("BBB") == 75


class TestCheckoutOffer3(unittest.TestCase):
    def test_checkout(self):
        assert checkout("BBCB") == 95


class TestCheckoutOfferOneFree(unittest.TestCase):
    def test_checkout(self):
        assert checkout("EE") == 80


class TestCheckoutOfferEEE(unittest.TestCase):
    def test_checkout(self):
        assert checkout("EEE") == 120


class TestCheckoutOfferOneFree1(unittest.TestCase):
    def test_checkout(self):
        assert checkout("EEB") == 80


class TestCheckoutOfferOneFree2(unittest.TestCase):
    def test_checkout(self):
        assert checkout("EEEB") == 120


class TestCheckoutOffer5A(unittest.TestCase):
    def test_checkout(self):
        assert checkout("AAAAA") == 200


class TestCheckoutOfferF(unittest.TestCase):
    def test_checkout(self):
        assert checkout("FFF") == 20


class TestCheckoutOfferF(unittest.TestCase):
    def test_checkout(self):
        assert checkout("FF") == 20


if __name__ == '__main__':
    unittest.main()
