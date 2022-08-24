"""Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:

track = Track(start_x, start_y)

где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)

где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); max_speed - максимальная скорость
на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:

add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:

track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2  # True, если длина пути для track1 больше, чем для track2
track1 < track2  # True, если длина пути для track1 меньше, чем для track2

И функция:

n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track

Создайте два маршрута track1 и track2 с координатами:

1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.

P.S. На экран в программе ничего выводить не нужно."""


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.__to_x = to_x
        self.__to_y = to_y
        self.__max_speed = max_speed

    @property
    def x(self):
        return self.__to_x

    @property
    def y(self):
        return self.__to_y

    @property
    def max_speed(self):
        return self.__max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.__start_x = start_x
        self.__start_y = start_y
        self.__tracks = []

    def get_tracks(self):
        return tuple(self.__tracks)

    def add_track(self, tr):
        self.__tracks.append(tr)

    def __len__(self):
        len_1 = ((self.__start_x - self.__tracks[0].x) ** 2 + (self.__start_y - self.__tracks[0].y) ** 2) ** 0.5
        return int(len_1 + sum(self.__get_length(i) for i in range(1, len(self.__tracks))))

    def __get_length(self, value):
        return ((self.__tracks[value-1].x - self.__tracks[value].x) ** 2 + (self.__tracks[value-1].y - self.__tracks[value].y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)



track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
