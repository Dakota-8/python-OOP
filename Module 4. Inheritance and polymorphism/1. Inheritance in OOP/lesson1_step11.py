"""
Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, ..., xN)

где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

С объектами этого класса должны выполняться команды:

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами

Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:

raise TypeError('размерности векторов не совпадают')

В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:

v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')

При операциях сложения и вычитания с объектом класса VectorInt:

v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt

должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной. Иначе, v
должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Vector:
    _types = (int, float)

    def __init__(self, *args):
        self.__check_coords(args)
        self._coords = args

    def __check_coords(self, coords):
        if not all(type(x) in self._types for x in coords):
            raise ValueError('неверный тип координат')

    def get_coords(self):
        return tuple(self._coords)

    def __check_dimension(self, item):
        if len(self._coords) != len(item.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__check_dimension(other)
        coords = tuple(a + b for a, b in zip(self._coords, other.get_coords()))
        return self.__make_vector(coords)

    def __sub__(self, other):
        self.__check_dimension(other)
        coords = tuple(a - b for a, b in zip(self._coords, other.get_coords()))
        return self.__make_vector(coords)


class VectorInt(Vector):
    _types = (int, )
