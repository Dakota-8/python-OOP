"""
Вы прошли магические методы. Начальство оценило вашу стойкость, рвение и решило дать вам испытание для подтверждения
уровня полученных навыков. Вам выпала великая честь создать полноценную программу игры в "Крестики-нолики". И вот перед
вами текст с заданием самого испытания.
Техническое задание

Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. Объекты этого класса
будут создаваться командой:

game = TicTacToe()

В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()

В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j

Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать
исключение командой:

raise IndexError('некорректно указанные индексы')

Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны
быть три публичных атрибута (атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)

В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном
случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть
в "Крестики-нолики" между человеком и компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.

P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.
"""
from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 'X'
    COMPUTER_O = 'O'

    def __init__(self):
        self._n = 3
        self._win = 0
        self.pole = [[Cell() for _ in range(self._n)] for _ in range(self._n)]

    def __check_index(self, index):
        if type(index) not in (tuple, list) or len(index) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = index
        if type(r) != int or not (0 <= r <= 2) or type(c) != int or not (0 <= c <= 2):
            raise IndexError('некорректно указанные индексы')

    def __update_win_status(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._win = 2
                return

        for i in range(self._n):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self._win = 2
                return

        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._n)) or \
                all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(self._n)):
            self._win = 1
            return
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._n)) or \
                all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(self._n)):
            self._win = 2
            return

        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self._win = 3

    def __getitem__(self, item):
        self.__check_index(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        r, c = key
        self.pole[r][c].value = value
        self.__update_win_status()

    def init(self):
        for row in self.pole:
            for x in row:
                x.value = self.FREE_CELL
        self._win = 0

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if x.value == 0 else x.value, row))
        print('----------------------------------------')

    def human_go(self):
        if not self:
            return
        while True:
            i, j = map(int, input('Ваш ход. Введите строку и столбец, куда вы ходите поставить крестик: ').split())
            if not (0 <= i < self._n) or not (0 <= j < self._n):
                continue
            if self[i, j] == self.FREE_CELL:
                self[i, j] = self.HUMAN_X
                break

    def computer_go(self):
        if not self:
            return

        while True:
            r = randint(0, self._n - 1)
            c = randint(0, self._n - 1)
            if self[r, c] != self.FREE_CELL:
                continue
            self[r, c] = self.COMPUTER_O
            break

    @property
    def is_human_win(self):
        return self._win == 1

    @property
    def is_computer_win(self):
        return self._win == 2

    @property
    def is_draw(self):
        return self._win == 3

    def __bool__(self):
        return self._win == 0 and self._win not in (1, 2, 3)
