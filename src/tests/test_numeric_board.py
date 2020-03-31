import unittest

from game.numeric.numeric_board import NumericBoard


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = NumericBoard()

    def test_check_column_win(self):
        board = NumericBoard()
        board.perform_move(0, 4)
        board.perform_move(3, 5)
        board.perform_move(6, 6)

        self.assertTrue(board.has_winning_pattern)

    def test_check_row_win(self):
        board = NumericBoard()
        board.perform_move(0, 4)
        board.perform_move(1, 5)
        board.perform_move(2, 6)

        self.assertTrue(board.has_winning_pattern)

    def test_check_first_diagonal_win(self):
        board = NumericBoard()
        board.perform_move(0, 4)
        board.perform_move(4, 5)
        board.perform_move(8, 6)

        self.assertTrue(board.has_winning_pattern)

    def test_check_second_diagonal_win(self):
        board = NumericBoard()
        board.perform_move(2, 4)
        board.perform_move(4, 5)
        board.perform_move(6, 6)

        self.assertTrue(board.has_winning_pattern)


if __name__ == '__main__':

    unittest.main(
        failfast=False,
        buffer=False,
        catchbreak=False)
