import inspect
import logging


class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("Logfile.log")  # file location
        fileformatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s ")  # logging format set
        fileHandler.setFormatter(fileformatter)  # giving format info to filehandler

        logger.addHandler(fileHandler)  # file handler object

        logger.setLevel(logging.DEBUG)
        return logger