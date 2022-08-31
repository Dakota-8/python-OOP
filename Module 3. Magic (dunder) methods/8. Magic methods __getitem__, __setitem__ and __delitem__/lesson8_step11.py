"""Подвиг 10. Вам необходимо описывать в программе очень большие и разреженные таблицы данных (с большим числом
пропусков). Для этого предлагается объявить класс SparseTable, объекты которого создаются командой:

st = SparseTable()

В каждом объекте этого класса должны создаваться локальные публичные атрибуты:

rows - общее число строк таблицы (начальное значение 0);
cols - общее число столбцов таблицы (начальное значение 0).

В самом классе SparseTable должны быть объявлены методы:

add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам row, col
(целые неотрицательные числа);
remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами (row, col).

При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, cols объекта класса
SparseTable. Если происходит попытка удалить несуществующую ячейку, то должно генерироваться исключение:

raise IndexError('ячейка с указанными индексами не существует')

Ячейки таблицы представляют собой объекты класса Cell, которые создаются командой:

data = Cell(value)

где value - данные ячейки (любой тип).

Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell.

Также с объектами класса SparseTable должны выполняться команды:

res = st[i, j] # получение данных из таблицы по индексам (i, j)
st[i, j] = value # запись новых данных по индексам (i, j)

Чтение данных возможно только для существующих ячеек. Если ячейки с указанными индексами нет, то генерировать исключение
командой:

raise ValueError('данные по указанным индексам отсутствуют')

При записи новых значений их следует менять в существующей ячейке или добавлять новую, если ячейка с индексами (i, j)
отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols).

Пример использования классов (эти строчки в программе не писать):

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно."""


class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.__table = {}

    def update_index(self):
        self.rows = max(key[0] for key in self.__table) + 1
        self.cols = max(key[1] for key in self.__table) + 1

    def add_data(self, row, col, data):
        self.__table[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            self.__table.pop((row, col))
            self.update_index()
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        try:
            return self.__table[(item[0], item[1])].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        item = (key[0], key[1])
        if item not in self.__table:
            self.__table[item] = Cell(value)
            self.update_index()
        else:
            self.__table[item] = Cell(value)
