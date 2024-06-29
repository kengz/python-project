from loguru import logger


def greet():
    return 'Hello world'


if __name__ == '__main__':
    logger.info(greet())
