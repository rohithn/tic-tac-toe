import unittest

from game.pattern.pattern_board import PatternBoard


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = PatternBoard()

    def test_board_columns(self):
        board = PatternBoard()
        board.perform_move(0, 1)
        board.perform_move(1, 2)
        board.perform_move(4, 1)
        board.perform_move(2, 2)
        board.perform_move(8, 1)
        expected_columns = [[1, 0, 0], [2, 1, 0], [2, 0, 1]]
        self.assertEqual(expected_columns, board.columns)

    def test_check_column_win(self):
        board = PatternBoard()
        board.perform_move(0, 1)
        board.perform_move(3, 1)
        board.perform_move(6, 1)

        self.assertTrue(board.has_winning_pattern)

    def test_check_row_win(self):
        board = PatternBoard()
        board.perform_move(0, 1)
        board.perform_move(1, 1)
        board.perform_move(2, 1)

        self.assertTrue(board.has_winning_pattern)

    def test_check_first_diagonal_win(self):
        board = PatternBoard()
        board.perform_move(0, 1)
        board.perform_move(4, 1)
        board.perform_move(8, 1)

        self.assertTrue(board.has_winning_pattern)

    def test_check_second_diagonal_win(self):
        board = PatternBoard()
        board.perform_move(2, 1)
        board.perform_move(4, 1)
        board.perform_move(6, 1)

        self.assertTrue(board.has_winning_pattern)

    def test_check_possible_move_locations(self):
        board = PatternBoard()
        board.perform_move(0, 1)
        board.perform_move(1, 2)
        board.perform_move(2, 1)

        self.assertEqual([3, 4, 5, 6, 7, 8], board.possible_move_locations)


if __name__ == '__main__':

    unittest.main(
        failfast=False,
        buffer=False,
        catchbreak=False)
