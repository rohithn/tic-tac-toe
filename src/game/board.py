from abc import abstractmethod
from itertools import product


class Board:
    """Class that represents a Tic-Tac-Toe game board.
    This should be subclassed to create variations of the game."""

    def __init__(self):
        """Represents a game board. Zeroes represent empty spaces."""
        self.board = [0 for _ in range(9)]

    def __str__(self):
        """Prints the board."""
        out = '-------------\n'
        for i, val in enumerate(self.board):
            item = '' if val == 0 else val
            out += '| ' + '{0:>1}'.format(item) + ' '
            if ((i + 1) % 3) == 0:
                out += '|\n'
        out += '-------------\n'
        return out

    def perform_move(self, move_location, move_value):
        """Updates the board with the new value at the specified location"""
        self.board[move_location] = move_value

    @property
    def rows(self):
        """Utility method to get all rows of the board."""
        rows = []
        for i in range(3):
            start_idx = i * 3
            end_idx = start_idx + 3
            rows.append(self.board[start_idx:end_idx])
        return rows

    @property
    def columns(self):
        """Utility method to get all columns of the board."""
        columns = []
        for i in range(3):
            column = self.board[i::3]
            columns.append(column)
        return columns

    @property
    def diagonals(self):
        """Utility method to get all diagonals of the board."""
        return [self.board[::4], self.board[2:7:2]]

    @property
    def possible_moves(self):
        """Returns all possible moves. A move is a tuple. The move[0] is the location
            (index) of the move and move[1] is the value."""
        return product(self.possible_move_locations, self.possible_move_values)

    @abstractmethod
    def has_winning_pattern(self) -> bool:
        """Defines the logic for the win state of the board.
        This abstract method should be implemented by the subclass."""
        pass

    @property
    @abstractmethod
    def possible_move_locations(self):
        """Defines the logic and returns the list of possible move locations.
        This abstract method should be implemented by the subclass."""
        pass

    @property
    @abstractmethod
    def possible_move_values(self):
        """Defines the logic and returns the list of possible move values.
        This abstract method should be implemented by the subclass."""
        pass
