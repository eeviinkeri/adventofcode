import unittest
from part1 import check_valid_numbers


data = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576
        ]

class TestValidationFunctions(unittest.TestCase):

    def test_check_valid_numbers(self):
        self.assertEqual(check_valid_numbers(data, 5), 127)


if __name__ == '__main__':
    unittest.main()
