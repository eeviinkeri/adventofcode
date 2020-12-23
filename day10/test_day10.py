import unittest
from part1 import add_outlet_and_device_joltages, get_num_of_adapters


class TestValidationFunctions(unittest.TestCase):

    def test_get_num_of_adapters(self):
        data = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3
        ]
        data = add_outlet_and_device_joltages(data)
        self.assertEqual(get_num_of_adapters(data, 1), 22)
        self.assertEqual(get_num_of_adapters(data, 3), 10)


if __name__ == '__main__':
    unittest.main()
