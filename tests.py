import unittest

from conway import Conway

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Conway(0, 0, num_rows, num_cols)
        self.assertEqual(
            len(m1._game_board),
            num_cols,
        )
        self.assertEqual(
            len(m1._game_board[0]),
            num_rows,
        )
        print(m1)
    

if __name__ == "__main__":
    unittest.main()