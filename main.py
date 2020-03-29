import time

from factory.game_factory import Game, GameFactory
from utils.enums import GameType, GameMode
from utils.logger import Logger

# Logger instance for logging errors
logger = Logger.get_logger('Tic-Tac-Toe')


def get_time():
    return time.ctime()


def main():
    """Main entry point of the script"""

    logger.info("Starting game: %s" % get_time())
    playing_time = time.time()

    print("::TIC-TAC-TOE::")

    while True:
        game_factory = prompt_user_game_type()
        game = prompt_user_game_mode(game_factory)
        game.start()

        play_again = input('Do you want to play again? (Y/n) : ')

        if play_again.capitalize() == 'N':
            break

    print('Thank you for playing!')

    logger.info("Game stopped: %s" % get_time())
    logger.info('Played for %s sec', time.time() - playing_time)
    Logger.shutdown()


def prompt_user_game_type() -> GameFactory:

    game_type = None

    while game_type is None:

        game_type = input("Choose game : (1) Pattern or (2) Numeric : ")

        if game_type == '1':
            return GameFactory.get_factory(GameType.PATTERN)
        elif game_type == '2':
            return GameFactory.get_factory(GameType.NUMBER)
        else:
            print('Invalid entry. Try again.')
            game_type = None


def prompt_user_game_mode(factory: GameFactory) -> Game:

    mode = None

    while mode is None:

        mode = input("Choose mode : (1) Single player or (2) Multi player : ")

        if mode == '1':
            return factory.create_game(GameMode.SINGLE_PLAYER)
        elif mode == '2':
            return factory.create_game(GameMode.MULTI_PLAYER)
        else:
            print('Invalid entry. Try again.')
            mode = None


if __name__ == '__main__':
    main()
