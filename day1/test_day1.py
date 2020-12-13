import unittest
from part1 import find_two_entries_that_sum_to_2020

class TestValidationFunctions(unittest.TestCase):

    def test_find_two_entries_that_sum_to_2020(self):
        data = [
            1721,
            979,
            366,
            299,
            675,
            1456
        ]
        self.assertEqual(find_two_entries_that_sum_to_2020(data), (1721, 299))


if __name__ == '__main__':
    unittest.main()
