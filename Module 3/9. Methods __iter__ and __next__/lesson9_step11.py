"""
Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны
создаваться командой:

m1 = Matrix(rows, cols, fill_value)

где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы (должно
быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

Также объекты можно создавать командой:

m2 = Matrix(list2D)

где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D не
прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')

Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение

Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')

Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать
исключение:

raise IndexError('недопустимые значения индексов')

Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1

Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц не совпадают
(разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')

Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""


class Matrix:
    def __init__(self, rows_or_lst, cols=0, fill_value=0):
        if type(rows_or_lst) == list:
            self.rows = len(rows_or_lst)
            self.cols = len(rows_or_lst[0])

            if not all(len(r) == self.cols for r in rows_or_lst) or \
                    not all(self.__is_digit(x) for row in rows_or_lst for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из цифр')

            self.__matrix = rows_or_lst

        else:
            if type(rows_or_lst) != int or type(cols) != int or type(fill_value) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

            self.rows, self.cols = rows_or_lst, cols
            self.__matrix = [[fill_value for _ in range(cols)] for _ in range(rows_or_lst)]

    @staticmethod
    def __is_digit(x):
        return type(x) in (int, float)

    def __check_index(self, indx):
        r, c = indx
        if not (0 <= r < self.rows) or not (0 <= c < self.cols):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.__matrix[r][c]

    def __setitem__(self, key, value):
        self.__check_index(key)
        if not self.__is_digit(value):
            raise TypeError('значения матрицы должны быть числами')

        r, c = key
        self.__matrix[r][c] = value

    def __check_dimensions(self, m):
        rows, cols = m.rows, m.cols
        if self.rows != rows or self.cols != cols:
            raise ValueError('операции возможно только с матрицами равных размеров')

    def __add__(self, other):
        if type(other) == type(self):
            self.__check_dimensions(other)
            return Matrix([[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(other) == type(self):
            self.__check_dimensions(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] - other for j in range(self.cols)] for i in range(self.rows)])
        