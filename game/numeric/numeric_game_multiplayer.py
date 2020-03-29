from game.game import Game
from game.numeric.numeric_board import NumericBoard
from game.numeric.numeric_player import NumericPlayer


class NumericMultiPlayerGame(Game):

    def __init__(self):
        super().__init__(NumericBoard())

    def start(self):
        print('Started Game :: Numeric (Multi Player)')

        player_1 = NumericPlayer('Odd', is_human=1, is_first=True)
        player_2 = NumericPlayer('Even', is_human=1, is_first=False)

        self.play([player_1, player_2])
