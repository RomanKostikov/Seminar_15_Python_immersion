# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
import logging
from datetime import datetime, date

logging.basicConfig(filename='Task4.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

months = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5, 'июн': 6, 'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10,
          'ноя': 11, 'дек': 12}
weekdays = {'пон': 1, 'вто': 2, 'сре': 3, 'чет': 4, 'пят': 5, 'суб': 6, 'вос': 7}


def text_to_date(text: str):
    '''Переводим текст в объект дату'''
    try:
        year = datetime.now().year  # 2023
        count, weekday_, month_ = text.split()  # 3-я среда мая - текстовый формат
        month = months[month_[:3]]  # 5 - число
        weekday = weekdays[weekday_[:3]] - 1  # 2 - число
        count = int(count[0])
    except Exception as exc:
        logger.info(f'{count}-й  {weekday_}  {month_} {year} =  ошибка: {exc}')

    count_week = 0
    for day in range(1, 31 + 1):
        result = date(year=year, month=month, day=day)
        if result.weekday() == weekday:
            count_week += 1
            if count_week == count:
                logger.info(f'{count}-й {weekday_} {month_} {year} = {result} ')
                return result


if __name__ == '__main__':
    print('9-й вторник мая:', text_to_date('9-й понедельник май'))
    print('1-й четверг ноября:', text_to_date('1-й четверг ноября'))
    print('4-я среда мая:', text_to_date('4-я среда май'))
