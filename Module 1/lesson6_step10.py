"""Подвиг 9 (на повторение материала). Объявите класс Point для представления точек на плоскости. Создавать объекты
этого класса предполагается командой:

pt = Point(x, y)

Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом объекте этого класса создаются локальные
свойства x, y, которые хранят конкретные координаты точки.

Необходимо в классе Point реализовать метод clone(self), который бы создавал новый объект класса Point как полную копию
текущего объекта (с тем же набором и значениями всех локальных свойств).

Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов метода clone."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(1, 2)
pt_clone = pt.clone()
