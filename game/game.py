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

            print(player_1.name + "'s turn")

            move_location_1, move_value_1 = player_1.get_move(self.board)
            self.board.perform_move(move_location_1, move_value_1)

            print(self.board)

            if self.board.has_winning_pattern:
                print(player_1.name + ' wins!')
                break
            if len(list(self.board.possible_moves)) == 0:
                print('Draw!')
                break

            print(player_2.name + "'s turn")

            move_location_2, move_value_2 = player_2.get_move(self.board)
            self.board.perform_move(move_location_2, move_value_2)

            print(self.board)

            if self.board.has_winning_pattern:
                print(player_2.name + ' wins!')
                break
            if len(list(self.board.possible_moves)) == 0:
                print('Draw!')
                break

    @staticmethod
    def get_players(players):
        first = second = None
        for player in players:
            if player.is_first:
                first = player
            else:
                second = player
        return first, second
