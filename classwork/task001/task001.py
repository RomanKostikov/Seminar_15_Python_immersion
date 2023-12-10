# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

# Configure the logging module to write to a file
logging.basicConfig(filename='error.log', level=logging.ERROR)

try:
    # Perform the division operation
    result = 10 / 0
except ZeroDivisionError as e:
    # Log the error message to the file
    logging.error('Error occurred: {}'.format(e))
