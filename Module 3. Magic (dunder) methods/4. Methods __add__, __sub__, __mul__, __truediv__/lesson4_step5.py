"""Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:

lst = [1, 2, 3] + [4.5, -3.6, 0.78]

Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка, как это
показано в примере:

lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен
сохраняться)

Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты которого
создаются командами:

lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями

Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять
следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]

Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]"""


class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError('Правый операнд должен иметь тип list или NewList')
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))

    @staticmethod
    def __diff_list(lst_1, lst_2):
        if len(lst_2) == 0:
            return lst_1
        temp_lst1 = [(i, type(i)) for i in lst_1]
        temp_lst2 = [(i, type(i)) for i in lst_2]
        for i in temp_lst2:
            if i in temp_lst1:
                temp_lst1.remove(i)
        return [i[0] for i in temp_lst1]

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError('Правый операнд должен иметь тип list или NewList')
        return NewList(self.__diff_list(other, self._lst))

    def get_list(self):
        return self._lst


    """
class NewList(list):

    def __sub__(self, other):
        tmp_lst = [(i, type(i)) for i in self]
        for i in [(i, type(i)) for i in other]:
            if i in tmp_lst:
                tmp_lst.remove(i)
        return NewList(i[0] for i in tmp_lst)

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        return self
        """
