import logging
logging.basicConfig(
    format='%(asctime)s  %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%y %H:%M:%S',
    level=logging.DEBUG,
    filename='log.txt'
)
logger = logging.getLogger('bookstore_app')
logger.setLevel(logging.DEBUG)
logger.info("Logging is set up.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")