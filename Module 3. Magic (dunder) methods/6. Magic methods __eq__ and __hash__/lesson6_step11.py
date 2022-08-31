"""Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)

где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие
дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе,
генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")

Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться
условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")

Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)),
где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle."""


class TriangleDescriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and value >= 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Triangle:
    a = TriangleDescriptor()
    b = TriangleDescriptor()
    c = TriangleDescriptor()

    def __init__(self, a, b, c):
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
