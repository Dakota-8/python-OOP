"""Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:

dt = DeltaClock(clock1, clock2)

где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться
командой:

clock = Clock(hours, minutes, seconds)

где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды

Если разность получается отрицательной, то разницу времен считать нулевой.

Пример использования классов (эти строчки в программе писать не нужно):

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400

Обратите внимание, добавляется незначащий ноль, если число меньше 10."""


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, first_clock, second_clock):
        self._clock1 = first_clock
        self._clock2 = second_clock


    def __len__(self):
        diff = self._clock1.get_time() - self._clock2.get_time()
        return diff if diff > 0 else 0

    def __str__(self):
        d = self.__len__()
        hours = d // 3600
        minutes = d % 3600 // 60
        seconds = d % 3600 % 60
        return f"{str(hours).zfill(2)}: {str(minutes).zfill(2)}: {str(seconds).zfill(2)}"


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
str_dt = str(dt)
print(str_dt)
