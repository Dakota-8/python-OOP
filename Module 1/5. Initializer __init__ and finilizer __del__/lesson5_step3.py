"""Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)

Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте)
money каждого экземпляра класса.

P.S. На экран в программе ничего выводить не нужно."""


class Translator:
    def __init__(self):
        self.dictionary = {}

    def add(self, eng, rus):
        self.dictionary.setdefault(eng, []).append(rus)

    def remove(self, eng):
        self.dictionary.pop(eng)

    def translate(self, eng):
        return self.dictionary[eng]


class Money:
    def __init__(self, Money=0):
        self.money = Money


my_money = Money(100)
your_money = Money(1000)
