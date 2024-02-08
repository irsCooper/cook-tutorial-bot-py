import logging

INFO = "info"
DEBUG = "debug"

name = "log"


async def create_logger(levl: str):
    logger = logging.getLogger(name=name)
    if levl == INFO:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)
        
    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - [%(levelname)s] %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    

LOGER = logging.getLogger(name=name)