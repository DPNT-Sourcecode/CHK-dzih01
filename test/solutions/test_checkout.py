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
        assert checkout("ACBxA") == -1


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


class TestCheckoutOfferF20(unittest.TestCase):
    def test_checkout(self):
        assert checkout("FFF") == 20


class TestCheckoutOfferF2(unittest.TestCase):
    def test_checkout(self):
        assert checkout("FF") == 20


class TestCheckoutOfferF4(unittest.TestCase):
    def test_checkout(self):
        assert checkout("FFFF") == 30


class TestCheckoutOfferF6(unittest.TestCase):
    def test_checkout(self):
        assert checkout("FFFFFF") == 40


class TestCheckoutOfferLong(unittest.TestCase):
    def test_checkout(self):
        assert checkout("ABCDEFABCDEF") == 300


class TestCheckoutOfferLong1(unittest.TestCase):
    def test_checkout(self):
        assert checkout("CDFFAECBDEAB") == 300


class TestCheckoutFullShop(unittest.TestCase):
    def test_checkout(self):
        assert checkout("RRRQ") == 150


class TestCheckoutFullShop1(unittest.TestCase):
    def test_checkout(self):
        assert checkout("NNN") == 120


class TestCheckoutFullShopFreeM(unittest.TestCase):
    def test_checkout(self):
        assert checkout("NNNM") == 120


class TestCheckoutFullShopFreeM(unittest.TestCase):
    def test_checkout(self):
        assert checkout("V") == 50


class TestCheckoutGroupOffer(unittest.TestCase):
    def test_checkout(self):
        assert checkout("STX") == 45


class TestCheckoutGroupOffer1(unittest.TestCase):
    def test_checkout(self):
        assert checkout("STXYZS") == 90


class TestCheckoutGroupOffer2(unittest.TestCase):
    def test_checkout(self):
        assert checkout("SSS") == 45


class TestCheckoutGroupOffer3(unittest.TestCase):
    def test_checkout(self):
        assert checkout("SSSZ") == 65


class TestCheckoutGroupOffer4(unittest.TestCase):
    def test_checkout(self):
        assert checkout("ZZZ") == 45


class TestCheckoutGroupOffer5(unittest.TestCase):
    def test_checkout(self):
        assert checkout("STXS") == 62


class TestCheckoutGroupOffer6(unittest.TestCase):
    def test_checkout(self):
        assert checkout("STXZ") == 62


class TestCheckoutGroupOfferLong(unittest.TestCase):
    def test_checkout(self):
        assert checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1602


if __name__ == '__main__':
    unittest.main()
