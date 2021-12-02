import unittest
from part1 import move_x_right_1_down
from part2 import move_1_right_2_down


test_data = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#' 
]


class TestFunctions(unittest.TestCase):

    def test_move_x_right_1_down(self):
        self.assertEqual(move_x_right_1_down(test_data, 1), 2)
    def test_move_x_right_1_down(self):
        self.assertEqual(move_x_right_1_down(test_data, 3), 7)
    def test_move_x_right_1_down(self):
        self.assertEqual(move_x_right_1_down(test_data, 5), 3)
    def test_move_x_right_1_down(self):
        self.assertEqual(move_x_right_1_down(test_data, 7), 4)
    def test_move_x_right_1_down(self):
        self.assertEqual(move_1_right_2_down(test_data), 2)

if __name__ == '__main__':
    unittest.main()
