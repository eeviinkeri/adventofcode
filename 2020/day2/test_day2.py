import unittest
import part1
import part2



class TestValidationFunctions(unittest.TestCase):

    def test_validate(self):

        self.assertTrue(part1.validate('1-3 a abcde'))
        self.assertFalse(part1.validate('1-3 b cdefg'))
        self.assertTrue(part1.validate('2-9 c ccccccccc'))

        self.assertTrue(part2.validate('1-3 a abcde'))
        self.assertFalse(part2.validate('1-3 b cdefg'))
        self.assertFalse(part2.validate('2-9 c ccccccccc'))


if __name__ == '__main__':
    unittest.main()
