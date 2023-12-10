# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.
import logging
import sys
from typing import Callable
from functools import wraps
from venv import logger

logging.basicConfig(filename='error.log',
                    level=logging.NOTSET,
                    format='[{levelname:<8}]{asctime}: {funcName} -> {msg}', style='{')


def log_errors(func: Callable) -> Callable:
    logger = logging.getLogger(func.__name__)
    logger.addHandler(logging.StreamHandler(sys.stdout))

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        logger.info(f'{args}, {kwargs}: {result}')

    return wrapper


@log_errors
def add_numbers(*args, **kwargs):
    return sum(args)


add_numbers(1, 2, 3, 4, 5, a=1, b=2, c=3)
