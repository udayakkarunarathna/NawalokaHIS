import unittest
from main import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, CI/CD!")

if __name__ == '__main__':
    unittest.main()



