import unittest
from part1 import validate_required_fields
from part2 import birth_year_is_valid, height_is_valid, hair_color_is_valid, eye_color_is_valid, passport_id_is_valid


class TestValidationFunctions(unittest.TestCase):

    def test_validate_required_fields(self):
        self.assertTrue(validate_required_fields(
            'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'))
        self.assertFalse(validate_required_fields(
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'))
        self.assertTrue(validate_required_fields(
            'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'))
        self.assertFalse(validate_required_fields(
            'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'))

    def test_birth_year_is_valid(self):
        self.assertTrue(birth_year_is_valid('2002'))
        self.assertFalse(birth_year_is_valid('2003'))

    def test_height_is_valid(self):
        self.assertTrue(height_is_valid('60in'))
        self.assertTrue(height_is_valid('190cm'))
        self.assertFalse(height_is_valid('190in'))
        self.assertFalse(height_is_valid('190'))

    def test_hair_color_is_valid(self):
        self.assertTrue(hair_color_is_valid('#123abc'))
        self.assertFalse(hair_color_is_valid('#123abz'))
        self.assertFalse(hair_color_is_valid('123abc'))

    def test_eye_color_is_valid(self):
        self.assertTrue(eye_color_is_valid('brn'))
        self.assertFalse(eye_color_is_valid('wat'))

    def test_passport_id_is_valid(self):
        self.assertTrue(passport_id_is_valid('000000001'))
        self.assertFalse(passport_id_is_valid('0123456789'))


if __name__ == '__main__':
    unittest.main()
