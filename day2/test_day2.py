import unittest
from part1 import validate


class TestValidationFunctions(unittest.TestCase):

    def test_validate(self):
        self.assertTrue(validate('1-3 a abcde'))
        self.assertFalse(validate('1-3 b cdefg'))
        self.assertTrue(validate('2-9 c ccccccccc'))


if __name__ == '__main__':
    unittest.main()
