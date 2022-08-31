"""Подвиг 9. Вам необходимо реализовать односвязный список из объектов класса ListObject:

Для этого объявите в программе класс ListObject, объекты которого создаются командой:

obj = ListObject(data)

Каждый объект класса ListObject должен содержать локальные свойства:

next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть, атрибут next_obj
объекта self должен ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))

Затем, создайте первый объект head_obj класса ListObject и сохраните в нем первую строку из списка lst_in. После этого
присоедините к head_obj (как это показано на рисунке) последующие объекты класса ListObject с соответствующими строками
из списка lst_in."""

import sys


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))
head_obj = ListObject(lst_in[0])
last_obj = head_obj
for i in range(1, len(lst_in)):
    new_obj = ListObject(lst_in[i])
    last_obj.link(new_obj)
    last_obj = new_obj
