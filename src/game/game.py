from abc import abstractmethod

from game.board import Board


class Game(object):
    """Base class for the Tic-Tac-Toe game."""

    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def start(self):
        """Main class that should be initialized."""
        pass

    def play(self, players):
        """Starts the game play logic.
        The play loops for both players until a win or draw state is reached."""

        player_1, player_2 = self.get_players(players)

        print(self.board)

        while True:

            """Player 1's turn"""
            print(player_1.name + "'s turn")

            """P1 - Get Move"""
            move_location_1, move_value_1 = player_1.get_move(self.board)

            """P1 - Perform Move, Value"""
            self.board.perform_move(move_location_1, move_value_1)

            print(self.board)

            """Check Board for Win/Draw"""
            if self.check_board_state_done(player_1):
                break

            """Player 2's turn"""
            print(player_2.name + "'s turn")

            """P2 - Get Move, Value"""
            move_location_2, move_value_2 = player_2.get_move(self.board)

            """P2 - Perform Move"""
            self.board.perform_move(move_location_2, move_value_2)

            print(self.board)

            """Check Board for Win/Draw"""
            if self.check_board_state_done(player_2):
                break

    def check_board_state_done(self, player) -> bool:
        """Check Board for Win/Draw"""
        if self.board.has_winning_pattern:
            print(player.name + ' wins!')
            return True
        if len(list(self.board.possible_moves)) == 0:
            print('Draw!')
            return True
        return False

    @staticmethod
    def get_players(players):
        """"Get first and second players"""
        first = second = None
        for player in players:
            if player.is_first:
                first = player
            else:
                second = player
        return first, second
