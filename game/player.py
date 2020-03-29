from abc import abstractmethod

from game.board import Board


class Player:
    """Abstract class for a Player."""

    def __init__(self, name, is_human, is_first=False):
        self.name = name
        self.is_human = is_human
        self.is_first = is_first

    def get_move(self, board: Board):
        if self.is_human:
            return self.get_move_from_user(board)
        else:
            return self.find_move_by_computer(board)

    @abstractmethod
    def get_move_from_user(self, board: Board):
        """Abstract methods that should read the input from the user."""
        pass

    @abstractmethod
    def find_move_by_computer(self, board: Board):
        """Abstract methods that should search for the best play by the computer."""
        pass
