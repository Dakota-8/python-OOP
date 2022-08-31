"""Подвиг 8. Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))

Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"

Например:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021

Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:

bs = BookStudy(name, author, year)

где name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число). Такие же
публичные локальные атрибуты должны быть в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in). После этого
определить число книг с уникальными хэшами. Это число сохранить через переменную unique_books (целое число).

P.S. На экран ничего выводить не нужно.

Sample Input:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021

Sample Output: """
import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_bs = []
for i in lst_in:
    args = list(map(str.strip, i.split(';')))
    args[-1] = int(args[-1])
    lst_bs.append(BookStudy(*args))

unique_books = len(set(hash(i) for i in lst_bs))
