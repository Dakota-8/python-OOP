"""Большой подвиг 5. Вам необходимо написать программу для удобного обращения с таблицами однотипных данных (чисел,
строк, булевых значений и т.п.), то есть, все ячейки таблицы должны представлять какой-то один указанный тип.

Для этого в программе необходимо объявить три класса:

TableValues - для работы с таблицей в целом;
CellInteger - для операций с целыми числами;
IntegerValue - дескриптор данных для работы с целыми числами.

Начнем с дескриптора IntegerValue. Это должен быть дескриптор данных (то есть, и для записи и считывания значений). Если
присваиваемое значение не является целым числом, должно генерироваться исключение командой:

raise ValueError('возможны только целочисленные значения')

Следующий класс CellInteger описывает одну ячейку таблицы для работы с целыми числами. В этом классе должен быть
публичный атрибут (атрибут класса):

value - объект дескриптора, класса IntegerValue.

А объекты класса CellInteger должны создаваться командой:

cell = CellInteger(start_value)

где start_value - начальное значение ячейки (по умолчанию равно 0 и сохраняется в ячейке через дескриптор value).

Наконец, объекты последнего класса TableValues создаются командой:

table = TableValues(rows, cols, cell=CellInteger)

где rows, cols - число строк и столбцов (целые числа); cell - ссылка на класс, описывающий работу с отдельными ячейками
таблицы. Если параметр cell не указан, то генерировать исключение командой:

raise ValueError('параметр cell не указан')

Иначе, в объекте table класса TableValues создается двумерный (вложенный) кортеж с именем cells размером rows x cols,
состоящий из объектов указанного класса (в данном примере - класса CellInteger).

Также в классе TableValues предусмотреть возможность обращения к отдельной ячейке по ее индексам, например:

value = table[1, 2] # возвращает значение ячейки с индексом (1, 2)
table[0, 0] = value # записывает новое значение в ячейку (0, 0)

Обратите внимание, по индексам сразу должно возвращаться значение ячейки, а не объект класса CellInteger. И то же самое
с присваиванием нового значения.

Пример использования классов (эти строчки в программе не писать):

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. В качестве домашнего задания создайте класс CellString для работы со строками и используйте тот же класс
TableValues для этого нового типа данных.

Последнее: дескрипторы здесь для повторения. В реальной разработке лучше использовать в таких задачах объекты-свойства
(property)."""


class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __check_index(self, index):
        row, col = index
        if type(row) != int or not (0 <= row < self.rows) or type(col) != int or not (0 <= col <= self.cols):
            raise ValueError('возможны только целочисленные значения')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.cells[key[0]][key[1]].value = value
