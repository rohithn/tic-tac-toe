from game.game import Game
from game.numeric.numeric_board import NumericBoard
from utils.logger import Logger


logger = Logger.get_logger('Tic-Tac-Toe')


class NumericSinglePlayerGame(Game):

    def __init__(self):
        logger.info('Initializing single player numeric game...')
        super().__init__(NumericBoard())

    def start(self):
        # print('Started Game :: Numeric (Multi Player)')

        # player_1 = NumericPlayer(is_human=1, is_first=True)
        #  player_2 = NumericPlayer(is_human=1, is_first=False)

        # self.play([player_1, player_2])

        print('Not implemented')