
from abc import abstractmethod

from game.game import Game
from utils.enums import GameType, GameMode
from game.numeric.numeric_game_multiplayer import NumericMultiPlayerGame
from game.numeric.numeric_game_singleplayer import NumericSinglePlayerGame
from game.pattern.pattern_game_multiplayer import PatternMultiPlayerGame
from game.pattern.pattern_game_singleplayer import PatternSinglePlayerGame


class GameFactory(object):
    """The Abstract Factory interface declares a set of methods that return
    Factories for creating instance of a Numeric and Pattern game"""

    @staticmethod
    def get_factory(game_type: GameType):
        if game_type is GameType.PATTERN:
            return PatternGameFactory()
        elif game_type is GameType.NUMBER:
            return NumericGameFactory()

    @abstractmethod
    def create_game(self, mode: GameMode) -> Game:
        pass


class NumericGameFactory(GameFactory):
    """Factory for Numeric game. Based on the input, it creates
    instance of Single Player or Multi Player game"""

    def create_game(self, mode: GameMode) -> Game:
        if mode is GameMode.SINGLE_PLAYER:
            return NumericSinglePlayerGame()
        elif mode is GameMode.MULTI_PLAYER:
            return NumericMultiPlayerGame()
        else:
            raise ValueError('Mode not supported')


class PatternGameFactory(GameFactory):
    """Factory for Pattern game. Based on the input, it creates
        instance of Single Player or Multi Player game"""

    def create_game(self, mode: GameMode) -> Game:
        if mode is GameMode.SINGLE_PLAYER:
            return PatternSinglePlayerGame()
        elif mode is GameMode.MULTI_PLAYER:
            return PatternMultiPlayerGame()
        else:
            raise ValueError('Mode not supported')
