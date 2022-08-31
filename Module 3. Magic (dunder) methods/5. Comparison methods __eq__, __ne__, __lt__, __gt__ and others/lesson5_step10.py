"""

Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)

где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела
(число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5

Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно.
"""


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.body_weight = self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, (int, Body)):
            if isinstance(other, int):
                return self.body_weight == other
            else:
                return self.body_weight == other.body_weight

    def __lt__(self, other):
        if isinstance(other, (int, Body)):
            if isinstance(other, int):
                return self.body_weight < other
            else:
                return self.body_weight < other.body_weight
