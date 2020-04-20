import logging
import inspect

class TestLog:
    
    def getLogger(self):

        loggerName = inspect.stack()[1][3]    
        logger=logging.getLogger(loggerName)

        fileHandler=logging.FileHandler('testlog.log')
        formatter=logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)

        return logger