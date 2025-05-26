import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        
    def test_cell_points(self):
        num_cols = 10
        num_rows = 10
        start_x = 50
        start_y = 50
        size_x = 50
        size_y = 50
        m1 = Maze(start_x, start_y, num_rows, num_cols, size_x, size_y)
        first_cell = m1._Maze__cells[0][0]
        first_cell.draw(start_x, start_y, start_x + size_x, start_y + size_y)

        self.assertEqual(
            first_cell._Cell__x1,
            50
        )

        self.assertEqual(
            first_cell._Cell__y1,
            50
        )

        self.assertEqual(
            first_cell._Cell__x2,
            100
        )

        self.assertEqual(
            first_cell._Cell__y2,
            100
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrace_and_exit()
        first_cell = m1._Maze__cells[0][0]
        last_cell = m1._Maze__cells[num_cols - 1][num_rows - 1]

        self.assertFalse(first_cell.has_top_wall)
        self.assertTrue(first_cell.has_right_wall)
        self.assertTrue(first_cell.has_left_wall)
        self.assertTrue(first_cell.has_bottom_wall)

        self.assertTrue(last_cell.has_top_wall)
        self.assertTrue(last_cell.has_right_wall)
        self.assertTrue(last_cell.has_left_wall)
        self.assertFalse(last_cell.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()