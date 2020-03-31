import logging


class Logger(object):

    __instance = None

    def __init__(self, level):
        """Virtually private constructor."""
        if Logger.__instance is not None:
            raise Exception("Multiple instance of this class is not allowed.")
        else:
            logging.basicConfig(format='%(asctime)s - %(name)s - [ %(levelname)s ] - %(message)s',
                                level=self.__get_level(level))
            Logger.__instance = self

    @staticmethod
    def get_logger(name, level="INFO"):
        if Logger.__instance is None:
            Logger(level)
        return logging.getLogger(name)

    @staticmethod
    def __get_level(level):
        if level.upper() == "INFO":
            return logging.INFO
        elif level.upper() == "ERROR":
            return logging.ERROR
        else:
            return logging.DEBUG

    @staticmethod
    def shutdown():
        logging.shutdown()
