import unittest
from lab07 import *

class TestMyRecursion(unittest.TestCase):
    def test_one(self):
        self.assertEqual(one(1), 1)
        self.assertEqual(one(2), 3)
        self.assertEqual(one(4), 10)
    def test_two(self):
        self.assertEqual(two(1, 1), 1)
        self.assertEqual(two(2, 1), 2)
        self.assertEqual(two(2, 2), 4)
        self.assertEqual(two(3, 5), 243)
    def test_three(self):
        self.assertEqual(three(1), "1")
        self.assertEqual(three(2), "2 1")
        self.assertEqual(three(5), "5 4 3 2 1")

if __name__ == '__main__':
    unittest.main()
