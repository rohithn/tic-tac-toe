from game.board import Board
from utils.logger import Logger

logger = Logger.get_logger('Tic-Tac-Toe')


class PatternBoard(Board):

    def __init__(self):
        super().__init__()
        self.values = range(1, 3)  # [1, 2] - 1 for X, 2 for O

    def __str__(self):
        out = '-------------\n'
        for i, val in enumerate(self.board):
            item = 'X' if val == 1 else 'O' if val == 2 else ''
            out += '| ' + '{0:>1}'.format(item) + ' '
            if ((i + 1) % 3) == 0:
                out += '|\n'
        out += '-------------\n'
        return out

    @property
    def has_winning_pattern(self):
        """Implemented abstract method"""
        """Returns True if the patterns match in row, column or diagonal"""
        winning_patterns = [
            self.row_has_winning_pattern,
            self.column_has_winning_pattern,
            self.diagonal_has_winning_pattern
        ]
        return any(winning_patterns)

    @property
    def row_has_winning_pattern(self):
        for row in self.rows:
            row = [val for val in row if val != 0]
            if row[1:] == row[:-1] and len(row) == 3:
                return True
        return False

    @property
    def column_has_winning_pattern(self):
        for column in self.columns:
            column = [val for val in column if val != 0]
            if column[1:] == column[:-1] and len(column) == 3:
                return True
        return False

    @property
    def diagonal_has_winning_pattern(self):
        for diagonal in self.diagonals:
            diagonal = [val for val in diagonal if val != 0]
            if diagonal[1:] == diagonal[:-1] and len(diagonal) == 3:
                return True
        return False

    @property
    def possible_move_locations(self):
        """Returns all indexes that contain the value zero"""
        return [i for i, val in enumerate(self.board) if val == 0]

    @property
    def possible_move_values(self):
        """Returns all possible values that can be placed on the board"""
        return [val for val in self.values]
