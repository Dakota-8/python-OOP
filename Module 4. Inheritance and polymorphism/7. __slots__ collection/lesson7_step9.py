"""
Подвиг 7. Объявите класс Note (нота), объекты которого создаются командой:

note = Note(name, ton)

где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си); ton - тональность ноты (целое число).
Тональность (ton) принимает следующие целые значения:

-1 - бемоль (flat);
0 - обычная нота (normal);
1 - диез (sharp).

Если в названии (name) или тональности (ton) передаются недопустимые значения, то генерируется исключение командой:

raise ValueError('недопустимое значение аргумента')

В каждом объекте класса Note должны формироваться локальные атрибуты с именами _name и _ton с соответствующими
значениями.

Объявите класс с именем Notes, в объектах которого разрешены только локальные атрибуты с именами (ограничение задается
через коллекцию __slots__):

_do - ссылка на ноту до (объект класса Note);
_re - ссылка на ноту ре (объект класса Note);
_mi - ссылка на ноту ми (объект класса Note);
_fa - ссылка на ноту фа (объект класса Note);
_solt - ссылка на ноту соль (объект класса Note);
_la - ссылка на ноту ля (объект класса Note);
_si - ссылка на ноту си (объект класса Note).

Объект класса Notes должен создаваться командой:

notes = Notes()

и быть только один (одновременно в программе два и более объектов класса Notes недопустимо). Используйте для этого
паттерн Singleton.

В момент создания объекта Notes должны автоматически создаваться перечисленные локальные атрибуты и ссылаться на
соответствующие объекты класса Note (тональность (ton) у всех нот изначально равна 0).

Обеспечить возможность обращения к нотам по индексам: 0 - до; 1 - ре; ... ; 6 - си. Например:

nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа

Если указывается недопустимый индекс (не целое число, или число, выходящее за интервал [0; 6]), то генерируется
исключение командой:

raise IndexError('недопустимый индекс')

Создайте в программе объект notes класса Notes.

P.S. В программе следует объявить только классы и создать объект notes. На экран выводить ничего не нужно.
"""


class Note:
    __slots__ = ('_name', '_ton')

    def __init__(self, name, ton):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and (type(value) != int or value not in (-1, 0, 1)):
            raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __cyrillic_notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        for i in range(len(self.__slots__)):
            setattr(self, self.__slots__[i], Note(self.__cyrillic_notes[i], 0))

    def __getitem__(self, item):
        if type(item) != int or not (-7 <= item < 7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])


notes = Notes()
