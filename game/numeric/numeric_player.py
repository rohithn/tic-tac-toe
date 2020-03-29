from game.board import Board
from game.player import Player


class NumericPlayer(Player):

    def __init__(self, name, is_human, is_first=False):
        super().__init__(name, is_human, is_first)

    def get_move_from_user(self, board):
        while True:
            try:
                # make locations human readable
                readable_locations = [i+1 for i in board.all_possible_move_locations]

                move_location = int(input('Enter move location {}: '.format(readable_locations))) - 1

                if move_location not in board.all_possible_move_locations:
                    print('Not a valid move location')
                else:
                    break

            except ValueError:
                print('Not a valid move location')

        while True:
            try:
                move_value = int(input('Enter move value {}: '.format(self.all_possible_move_values(board))))
                if move_value not in self.all_possible_move_values(board):
                    print('Not a valid move value')
                else:
                    break
            except ValueError:
                print('Not a valid move location')

        return move_location, move_value

    def all_possible_move_values(self, board):
        if self.is_first:
            return [value for value in board.all_possible_move_values if value % 2 == 1]
        else:
            return [value for value in board.all_possible_move_values if value % 2 == 0]

    def find_move_by_computer(self, board: Board):
        pass
