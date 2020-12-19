import unittest
from part1 import move_x_right_1_down


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
        self.assertEqual(move_x_right_1_down(test_data, 3), 7)

if __name__ == '__main__':
    unittest.main()
