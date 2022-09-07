"""
Подвиг 5. Объявите в программе класс Point, объекты которого должны создаваться командами:

pt = Point()
pt = Point(x, y)

где x, y - произвольные числа (координаты точки).

В каждом объекте класса Point должны формироваться локальные атрибуты _x, _y с соответствующими значениями. Если
аргументы не указываются (первая команда), то _x = 0, _y = 0.

Далее, в программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, булевы
величины (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются числами, то
формировать объект pt командой:

pt = Point(x, y)

Если хотя бы одно из значений не числовое, то формировать объект pt командой:

pt = Point()

Реализовать этот функционал с помощью блоков try/except. А в блоке finally вывести на экран сообщение в формате
(без кавычек):

"Point: x = <значение x>, y = <значение y>"
"""


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Point: x = {self._x}, y = {self._y}'


x, y = input().split()
pt = Point()
try:
    pt = Point(int(x), int(y))
except ValueError:
    try:
        pt = Point(float(x), float(y))
    except ValueError:
        pt = Point()
finally:
    print(pt)
