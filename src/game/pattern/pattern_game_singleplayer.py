from game.game import Game
from game.pattern.pattern_board import PatternBoard
from game.pattern.pattern_player import PatternPlayer


class PatternSinglePlayerGame(Game):

    def __init__(self):
        super().__init__(PatternBoard())

    def start(self):
        print('Started Game :: Pattern (Single Player)')

        human_player_first = input('Playing with dumb AI. Would you like to go first [Y/n]?:').lower()

        if human_player_first == '' or human_player_first == 'y':
            player_1 = PatternPlayer('X', is_human=True, is_first=True)
            player_2 = PatternPlayer('O', is_human=False, is_first=False)
        else:
            player_1 = PatternPlayer('X', is_human=False, is_first=True)
            player_2 = PatternPlayer('O', is_human=True, is_first=False)

        self.play([player_1, player_2])
