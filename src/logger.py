import logging
import sys
from logging.handlers import RotatingFileHandler
import main_helper


logger = logging.getLogger("infra_sim")

def setup_logging():
    logger.setLevel(logging.INFO)
    frmt = "%(asctime)s - %(levelname)s\t%(filename)s - %(funcName)s - %(message)s"
    my_fmt = logging.Formatter(frmt)

    #file handlers
    file_handler = RotatingFileHandler("logs/my_rotating_log.log", maxBytes=3000, backupCount=1) # will append logs to the file 
    file_handler.setFormatter(my_fmt)
    file_handler.setLevel(logging.DEBUG)

    #print handler
    print_handler = logging.StreamHandler(sys.stdout) # print to the terminal only errors and above
    print_handler.setLevel(logging.ERROR)

    #add handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(print_handler)

        logger.info("created log!")



main_helper.create_dir("logs")
setup_logging() 
