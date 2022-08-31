"""
Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)

где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list,
str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)

где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с
соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

При попытке записать данные другого типа (не совпадающего с атрибутом type_data объекта класса TableValues), должно
генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()

При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они выходят за
диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.__rows = rows
        self.__cols = cols
        self.__type_data = type_data
        self.__table = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def __iter__(self):
        for row in self.__table:
            yield (x.data for x in row)

    def __check_index(self, indx):
        r, c = indx
        if not (0 <= r < self.__rows) or not (0 <= c < self.__cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.__table[r][c].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if type(value) != self.__type_data:
            raise TypeError('неверный тип присваиваемых данных')
        r, c = key
        self.__table[r][c].data = value
