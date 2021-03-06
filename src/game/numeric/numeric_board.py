from game.board import Board


class NumericBoard(Board):

    def __init__(self):
        super().__init__()
        self.all_numbers = range(1, 10)
        self.winning_sum = 15

    @property
    def has_winning_pattern(self):
        """Implemented abstract method"""
        """Returns True if the sum is 15 in row, column or diagonal"""
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
            if sum(row) == self.winning_sum and len(row) == 3:
                return True
        return False

    @property
    def column_has_winning_pattern(self):
        for column in self.columns:
            column = [val for val in column if val != 0]
            if sum(column) == self.winning_sum and len(column) == 3:
                return True
        return False

    @property
    def diagonal_has_winning_pattern(self):
        for diagonal in self.diagonals:
            diagonal = [val for val in diagonal if val != 0]
            if sum(diagonal) == self.winning_sum and len(diagonal) == 3:
                return True
        return False

    @property
    def possible_move_locations(self):
        """Returns all indexes that contain the value zero"""
        return [i for i, val in enumerate(self.board) if val == 0]

    @property
    def possible_move_values(self):
        """Returns all possible values that can be placed on the board"""
        used_values = [val for val in self.board if val != 0]
        return [val for val in self.all_numbers if val not in used_values]
