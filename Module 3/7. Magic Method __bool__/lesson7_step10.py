"""Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)

где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает

При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными)
координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться
исключение командой:

raise ArithmeticError('размерности векторов не совпадают')

P.S. В программе на экран выводить ничего не нужно, только объявить класс."""


class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*(self.coords[i] + other.coords[i] for i in range(len(self.coords))))

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [i + other for i in self.coords]
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            self.coords = [self.coords[i] + other.coords[i] for i in range(len(self.coords))]
        return self

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [i - other for i in self.coords]
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            self.coords = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        return self

    def __mul__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coords[i] * other.coords[i] for i in range(len(self.coords))])

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.coords = [i - other for i in self.coords]
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            self.coords = [self.coords[i] - other.coords[i] for i in range(len(self.coords))]
        return self

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not any(list(filter(lambda x: self.coords[x] == other.coords[x], range(len(self.coords)))))


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
