from game.game import Game
from game.numeric.numeric_board import NumericBoard
from game.numeric.numeric_player import NumericPlayer


class NumericSinglePlayerGame(Game):

    def __init__(self):
        super().__init__(NumericBoard())

    def start(self):
        print('Started Game :: Numeric (Single Player)')

        human_player_first = input('Playing with dumb AI. Would you like to go first [Y/n]?:').lower()

        if human_player_first == '' or human_player_first == 'y':
            player_1 = NumericPlayer('Odd', is_human=True, is_first=True)
            player_2 = NumericPlayer('Even', is_human=False, is_first=False)
        else:
            player_1 = NumericPlayer('Odd', is_human=False, is_first=True)
            player_2 = NumericPlayer('Even', is_human=True, is_first=False)

        self.play([player_1, player_2])
