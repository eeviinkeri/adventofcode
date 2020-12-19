import unittest
from part1 import count_unique_letters


class TestFunctions(unittest.TestCase):

    def test_count_unique_letters(self):
        self.assertEqual(count_unique_letters('abc'), 3)
        self.assertEqual(count_unique_letters('abac'), 3)
        self.assertEqual(count_unique_letters('aaaa'), 1)
        self.assertEqual(count_unique_letters('b'), 1)


if __name__ == '__main__':
    unittest.main()
