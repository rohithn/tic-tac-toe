from game.board import Board
from game.player import Player


class PatternPlayer(Player):

    def __init__(self, name, is_human, is_first=False):
        super().__init__(name, is_human, is_first)
        self.name = name

    def get_move_from_user(self, board: Board):
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

        move_value = self.get_move_value()

        return move_location, move_value

    def find_move_by_computer(self, board: Board):
        pass

    def get_move_value(self):
        if self.is_first:
            return 1
        else:
            return 2
