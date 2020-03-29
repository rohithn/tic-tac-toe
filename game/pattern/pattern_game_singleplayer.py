from factory.game_factory import Game
from game.pattern.pattern_board import PatternBoard


class PatternSinglePlayerGame(Game):

    def __init__(self):
        super().__init__(PatternBoard())

    def start(self):
        print('Started Game :: Pattern (Single Player)')

        # player_1 = PatternPlayer(is_human=1, is_first=True, name='X')
        # player_2 = PatternPlayer(is_human=1, is_first=False, name='O')
        # self.play([player_1, player_2])

        print('Not implemented')
