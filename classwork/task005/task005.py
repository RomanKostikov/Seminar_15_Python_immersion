# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.
import argparse
from datetime import datetime

from classwork.task005.task004 import text_to_date

if __name__ == '__main__':
    months = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл', 8: 'авг', 9: 'сен', 10: 'окт',
              11: 'ноя', 12: 'дек'}
    weekdays = {1: 'вто', 2: 'сре', 3: 'чет', 4: 'пят', 5: 'суб', 6: 'вос', 7: 'пон'}

    parser = argparse.ArgumentParser(description="Получаем строку с датой")
    parser.add_argument('-count', type=str, default='1')
    parser.add_argument('-weekday', type=str, default='понeдельник')
    parser.add_argument('-month', type=str, default=months[datetime.now().month])

    args = parser.parse_args()

    weekday = weekdays[int(args.weekday)] if args.weekday.isdigit() and int(
        args.weekday) in weekdays else args.weekday  # неделю можно вводить числом
    month = months[int(args.month)] if args.month.isdigit() and int(
        args.month) in months else args.month  # месяц можно вводить числом

    print(f'{args.count} {weekday} {month}: ', text_to_date(f'{args.count} {weekday} {month}'))

    # запуск с командной строки: python ./task005.py -count='3-я' -weekday='среда'
    #  запуск с командной строки: python ./task005.py -count='3-я' -weekday=3
#  запуск с командной строки: python ./task005.py -count='3-я' -weekday=3 - month=3
