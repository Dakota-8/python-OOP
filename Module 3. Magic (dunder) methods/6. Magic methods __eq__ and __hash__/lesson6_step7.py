"""Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, weight, price)

где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число:
целое или вещественное).

Определите в этом классе магические методы:

__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
__eq__() - чтобы объекты с одинаковыми хэшами были равны.

Затем, из входного потока прочитайте строки командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))

Строки имеют следующий формат:

название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с именем
shop_items. Ключами словаря должны выступать сами объекты, а значениями - список в формате:

[item, total]

где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами). Подумайте, как
эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.

P.S. На экран ничего выводить не нужно, только объявить класс и сформировать словарь.

Sample Input:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Sample Output: """
import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = [item.rsplit(maxsplit=2) for item in lst_in]
lst = [ShopItem(name.strip(':'), w, p) for name, w, p in lst]

hash_lst = [hash(i) for i in lst]
shop_items = {item: [item, hash_lst.count(hash(item))] for item in lst}
