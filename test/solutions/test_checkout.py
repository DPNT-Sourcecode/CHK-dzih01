import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        #assert self.assertEqual(checkout("AC"), 70)
        assert checkout("AC") == 70

if __name__ == '__main__':
    unittest.main()
