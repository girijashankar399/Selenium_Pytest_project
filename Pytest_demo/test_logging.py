import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)


    fileHandler = logging.FileHandler("Logfile.log") #file location
    fileformatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s ") #logging format set
    fileHandler.setFormatter(fileformatter)    # giving format info to filehandler

    logger.addHandler(fileHandler) # file handler object

    logger.setLevel(logging.INFO)
    logger.debug("debug code executed")
    logger.info("Information statement")
    logger.warning("warning statement")
    logger.error("Error statement")
    logger.critical("Statement")
