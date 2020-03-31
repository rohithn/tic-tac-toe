from game.game import Game
from game.pattern.pattern_board import PatternBoard
from game.pattern.pattern_player import PatternPlayer


class PatternMultiPlayerGame(Game):

    def __init__(self):
        super().__init__(PatternBoard())

    def start(self):
        print('Started Game :: Pattern (Multi Player)')

        player_1 = PatternPlayer('X', is_human=1, is_first=True)
        player_2 = PatternPlayer('O', is_human=1, is_first=False)

        self.play([player_1, player_2])
