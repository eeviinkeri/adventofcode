import unittest
from part1 import find_two_entries_that_sum_to_2020
from part2 import find_three_entries_that_sum_to_2020


test_data = [
        1721,
        979,
        366,
        299,
        675,
        1456
    ]


class TestValidationFunctions(unittest.TestCase):

    def test_find_two_entries_that_sum_to_2020(self):
        self.assertEqual(find_two_entries_that_sum_to_2020(test_data), (1721, 299))

    def test_find_three_entries_that_sum_to_2020(self):
        self.assertEqual(find_three_entries_that_sum_to_2020(test_data), (979, 366, 675))


if __name__ == '__main__':
    unittest.main()
