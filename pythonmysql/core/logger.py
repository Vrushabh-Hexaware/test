import os
import logging
from .settings import settings

def config_logger():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    #create logger
    logger = logging.getLogger()
    logger.setLevel(settings.LOG_LEVEL)

    #create handler
    file_handler = logging.FileHandler(f'logs/{settings.LOG_FILE}', mode='a', encoding='utf-8')

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

logger = config_logger()