import argparse
from Matrix import Matrix
from Convert import convert_format
import logging

logging.basicConfig(filename='Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Получаем операцию над двумя матрицами")
    parser.add_argument('-m_1', type=list, action='append', default=
    [['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-m_2', type=list, action='append', default=
    [['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1']])
    parser.add_argument('-operation', type=str, default='*')

    args = parser.parse_args()

    m_1 = convert_format(args.m_1)
    m_2 = convert_format(args.m_2)

    if args.operation == '+':
        print(f'СЛОЖЕНИЕ: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) + Matrix(m_2)} '))
    elif args.operation == '*':
        print(f'УМНОЖЕНИЕ: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) * Matrix(m_2)} '))
    elif args.operation == '=':
        print(f'РАВЕНСТВО: {m_1} {args.operation} {m_2} = ', (f'{Matrix(m_1) == Matrix(m_2)} '))
    else:
        print(f'Такая операция {args.operation} над матрицами не предусмотрена!')
        logger.info(f'Такая операция {args.operation} над матрицами не предусмотрена!')

# Примеры вызова из командной строки(Log.log создается в корневой папке откуда вызывается приложение):
r""""
python homework/Matrix_terminal.py
python homework//Matrix_terminal.py -m_1='123 456 789' -m_2='123 456 789'
python homework/Matrix_terminal.py -m_1='123 456 789' -m_2='123 456 789' -operation='='
python homework//Matrix_terminal.py -m_1='123 456 789' -m_2='123 456 789' -operation='*'
"""


