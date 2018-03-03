import unittest

from lib.solutions.hello import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        friend_name = "Pepe"
        assert hello(friend_name) == "Hello, %s!" % friend_name


if __name__ == '__main__':
    unittest.main()
