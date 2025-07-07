import unittest
from utils import greet_user, add

class TestUtils(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("Alice"), "Hello, Alice! Welcome to the sample Python app.")

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

if __name__ == "__main__":
    unittest.main()
