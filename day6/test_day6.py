import unittest
from part1 import count_unique_letters
from part2 import count_yes_answers


class TestFunctions(unittest.TestCase):

    def test_count_unique_letters(self):
        self.assertEqual(count_unique_letters('abc'), 3)
        self.assertEqual(count_unique_letters('abac'), 3)
        self.assertEqual(count_unique_letters('aaaa'), 1)
        self.assertEqual(count_unique_letters('b'), 1)

    def test_count_yes_answers(self):
        self.assertEqual(count_yes_answers('abc', 1), 3)
        self.assertEqual(count_yes_answers('abc', 3), 0)
        self.assertEqual(count_yes_answers('abac', 2), 1)
        self.assertEqual(count_yes_answers('aaaa', 4), 1)
        self.assertEqual(count_yes_answers('b', 1), 1)


if __name__ == '__main__':
    unittest.main()
