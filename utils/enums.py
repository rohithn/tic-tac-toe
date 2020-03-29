import enum


class GameType(enum.Enum):
    PATTERN = 1
    NUMBER = 2


class GameMode(enum.Enum):
    SINGLE_PLAYER = 1
    MULTI_PLAYER = 2
