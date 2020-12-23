import unittest
from part1 import find_start_of_infinite_loop
from part2 import fix_program


data = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]


class TestFunctions(unittest.TestCase):

    def test_find_start_of_infinite_loop(self):
        self.assertEqual(find_start_of_infinite_loop(data, 0, [], 0), 5)

    def test_fix_program(self):
        self.assertEqual(fix_program(data), 8)


if __name__ == '__main__':
    unittest.main()
