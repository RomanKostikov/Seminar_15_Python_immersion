"""
Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.
На примере сравнение, умножение, сложение двух матриц.
"""

import logging

logging.basicConfig(filename='Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(
                f'Не возможно выполнить сложение матриц, размерности матриц несовместимы:  [{len(self._matr)}]'
                f'[{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}] ')
            # raise ValFormatError

        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in
                               range(len(self._matr))])
            logger.info(f' СЛОЖЕНИЕ:  {self._matr} + {other._matr} = {new_matr}  ')
            return new_matr

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            logger.error(
                f'Не возможно выполнить умножение матриц, размерности матриц несовместимы: [{len(self._matr)}]'
                f'[{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
            # raise ValFormatError
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in
                        self._matr]
            logger.info(f' УМНОЖЕНИЕ:  {self._matr} * {other._matr} = {new_matr}  ')
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.info(f' РАВЕНСТВО:  {self._matr} = {other._matr} = False ')
            return False
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        logger.info(f' РАВЕНСТВО:  {self._matr} = {other._matr} = False ')
                        return False
            logger.info(f' РАВЕНСТВО:  {self._matr} = {other._matr} = True ')
            return True

    # def __str__(self):
    #     s = ''
    #     for i in range(len(self._matr)):
    #         s += str(self._matr[i]) + '\n'
    #     return s

    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


if __name__ == '__main__':
    m_1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [-10, 11.5, 12]]

    m_2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [10, 11, 12]]

    m_3 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9],
           # [10, 11, 12, 13],
           [14, 15, 16, 17]]

    m_4 = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15]]

    print("Cложение матриц:")
    print(Matrix(m_1) + Matrix(m_2))
    # print(Matrix(m_3) + Matrix(m_1))

    print("Cравнение матриц:")
    print(Matrix(m_1) == Matrix(m_1))

    print("Умножение матриц:")
    print(Matrix(m_1) * Matrix(m_3))
    # print(Matrix(m_1) * Matrix(m_2))
