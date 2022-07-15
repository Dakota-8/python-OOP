"""Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:

cart = Cart()

Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки. Изначально этот список
должен быть пустым.

В классе Cart объявить методы:

add(self, gd) - добавление товара в корзину, представленного объектом gd;
remove(self, indx) - удаление товара из корзины по индексу indx;
get_list(self) - получение товаров корзины в виде списка из строк:

['<наименование_1>: <цена_1>',
'<наименование_2>: <цена_2>',
...
'<наименование_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:

Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:

gd = ИмяКласса(name, price)

Каждый объект классов товаров должен содержать локальные свойства:

name - наименование;
price - цена.

Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table), два ноутбука
(Notebook) и одну кружку (Cup). Названия и цены придумайте сами. """


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Samsung', 1000))
cart.add(TV('LG', 2500))
cart.add(Table('IKEA', 2000))
cart.add(Notebook('ASUS', 4000))
cart.add(Notebook('Acer', 3700))
cart.add(Cup('Cup', 50))

print(cart.get_list())
