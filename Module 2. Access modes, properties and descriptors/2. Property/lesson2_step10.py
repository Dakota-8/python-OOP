"""Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных
сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса будут
формироваться командой:

line = LineTo(x, y)

где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:

x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:

p = PathLines()                   # начало маршрута из точки 0, 0
p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0

где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:

get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется
как евклидовое расстояние по формуле:

L = sqrt((x1-x0)^2 + (y1-y0)^2)

где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. """


class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0), ) + args)

    def get_path(self):
        return self.coords[1:]

    def get_length(self):
        temp = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords)))
        return sum(map(lambda t: (((t[1].x - t[0].x) ** 2) + ((t[1].y - t[0].y) ** 2)) ** 0.5, temp))

    def add_line(self, line):
        self.coords.append(line)

class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(m)
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []