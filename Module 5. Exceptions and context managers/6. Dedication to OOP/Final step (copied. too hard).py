"""
Посвящение в ООП

Вы прошли серию испытаний и совершили множество подвигов, чтобы лицом к лицу столкнуться с настоящим вызовом, достойным
лишь избранных! Для подтверждения своих знаний и навыков вам предлагается пройти этап посвящения в
объектно-ориентированное программирование. И вот задание, которое выпало на вашу долю.

Руководство компании целыми днями не знает куда себя деть. Поэтому они решили дать задание своим программистам написать
программу игры "Морской бой". Но эта игра будет немного отличаться от классической. Для тех, кто не знаком с этой
древней, как мир, игрой, напомню ее краткое описание.

Каждый игрок у себя на бумаге рисует игровое поле 10 х 10 клеток и расставляет на нем десять кораблей:
однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1.

Корабли расставляются случайным образом, но так, чтобы не выходили за пределы игрового поля и не соприкасались друг с
другом (в том числе и по диагонали).

Затем, игроки по очереди называют клетки, куда производят выстрелы. И отмечают эти выстрелы на другом таком же поле в
10 х 10 клеток, которое представляет поле соперника. Соперник при этом должен честно отвечать: "промах", если ни один
корабль не был задет и "попал", если произошло попадание. Выигрывает тот игрок, который первым поразит все корабли
соперника.

Но это была игра из глубокого прошлого. Теперь же, в компьютерную эру, корабли на игровом поле могут перемещаться в
направлении своей ориентации на одну клетку после каждого хода соперника, если в них не было ни одного попадания.

Итак, лично вам поручается сделать важный фрагмент этой игры - расстановку и управление кораблями в этой игре. А само
задание звучит так.
Техническое задание

В программе необходимо объявить два класса:

Ship - для представления кораблей;
GamePole - для описания игрового поля.
Класс Ship

Класс Ship должен описывать корабли набором следующих параметров:

x, y - координаты начала расположения корабля (целые числа);
length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).

Объекты класса Ship должны создаваться командами:

ship = Ship(length)
ship = Ship(length, tp)
ship = Ship(length, tp, x, y)

По умолчанию (если не указывается) параметр tp = 1, а координаты x, y равны None.

В каждом объекте класса Ship должны формироваться следующие локальные атрибуты:

_x, _y - координаты корабля (целые значения в диапазоне [0; size), где size - размер игрового поля);
_length - длина корабля (число палуб);
_tp - ориентация корабля;
_is_move - возможно ли перемещение корабля (изначально равно True);
_cells - изначально список длиной length, состоящий из единиц (например, при length=3, _cells = [1, 1, 1]).

Список _cells будет сигнализировать о попадании соперником в какую-либо палубу корабля. Если стоит 1, то попадания не
было, а если стоит значение 2, то произошло попадание в соответствующую палубу.

При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по
игровому полю прекращается.

В самом классе Ship должны быть реализованы следующие методы (конечно, возможны и другие, дополнительные):

set_start_coords(x, y) - установка начальных координат (запись значений в локальные атрибуты _x, _y);
get_start_coords() - получение начальных координат корабля в виде кортежа x, y;
move(go) - перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку;
go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True;
is_collide(ship) - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или
пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение
есть и False - в противном случае;
is_out_pole(size) - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10);
возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;

С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к коллекции _cells следующим образом:

value = ship[indx] # считывание значения из _cells по индексу indx (индекс отсчитывается от 0)
ship[indx] = value # запись нового значения в коллекцию _cells

Класс GamePole

Следующий класс GamePole должен обеспечивать работу с игровым полем. Объекты этого класса создаются командой:

pole = GamePole(size)

где size - размеры игрового поля (обычно, size = 10).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_size - размер игрового поля (целое положительное число);
_ships - список из кораблей (объектов класса Ship); изначально пустой список.

В самом классе GamePole должны быть реализованы следующие методы (возможны и другие, дополнительные методы):

init() - начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship):
однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 (ориентация этих кораблей должна быть
случайной).

Корабли формируются в коллекции _ships следующим образом: однопалубных - 4; двухпалубных - 3; трехпалубных - 2;
четырехпалубный - 1. Ориентация этих кораблей должна быть случайной. Для этого можно воспользоваться функцией randint
следующим образом:

[Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]

Начальные координаты x, y не расставленных кораблей равны None.

После этого, выполняется их расстановка на игровом поле со случайными координатами так, чтобы корабли не пересекались
между собой.

get_ships() - возвращает коллекцию _ships;
move_ships() - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в
направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового
поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;
show() - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого
корабля, вода - значением 0);

get_pole() - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.

Пример отображения игрового поля:

0 0 1 0 1 1 1 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 1
0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0

Пример использования классов (эти строчки в программе не писать):

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()

В программе требуется только объявить классы Ship и GamePole с соответствующим функционалом. На экран выводить ничего
не нужно.

P.S. Для самых преданных поклонников программирования и ООП. Завершите эту программу, добавив еще один класс SeaBattle
для управления игровым процессом в целом. Игра должна осуществляться между человеком и компьютером. Выстрелы со стороны
компьютера можно реализовать случайным образом в свободные клетки. Сыграйте в эту игру и выиграйте у компьютера.
"""
from random import randint, choice
from time import sleep
from textwrap import dedent


class Ship:
    """Class for representing ships"""
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            elif self._tp == 2:
                self._y += go

    def is_collide(self, ship):
        ship_decks = set(ship.get_coords())
        return bool(self.area & ship_decks)

    @property
    def area(self):
        width = self._length if self._tp == 1 else 1
        height = self._length if self._tp == 2 else 1
        around_area = {(x, y) for x in range(self._x-1, self._x+width+1) for y in range(self._y-1, self._y+height+1)}
        return around_area

    def is_out_pole(self, size):
        coords = self.get_coords()
        coords = coords[0] + coords[-1]
        return not all(map(lambda n: 0 <= n < size, coords))

    def __getitem__(self, item):
        self._check_index(item)
        return self._cells[item]

    def __setitem__(self, key, value):
        self._check_index(key)
        if value not in (1, 2):
            raise ValueError("Cell values must be 1 or 2")
        self._cells[key] = value

    def _check_index(self, indx):
        if type(indx) is not int or indx < 0 or indx >= len(self._cells):
            raise IndexError("Wrong deck index")

    def __setattr__(self, key, value):
        if key in ('_x', '_y'):
            if value is not None:
                if type(value) is not int:
                    raise ValueError("Coordinates must be integers")

        if key == '_length' and value not in (1, 2, 3, 4):
            raise ValueError("Impossible number of decks")

        if key == '_tp' and value not in (1, 2):
            raise ValueError("Impossible ship direction")

        if key == '_is_move' and type(value) is not bool:
            raise ValueError("Attribute is_move takes only boolean values")

        super().__setattr__(key, value)

    @property
    def is_move(self):
        return self._is_move

    @is_move.setter
    def is_move(self, value):
        self._is_move = value

    @property
    def cells(self):
        return self._cells

    @property
    def tp(self):
        return self._tp

    def __len__(self):
        return self._length

    @property
    def is_alive(self):
        return any(map(lambda x: x == 1, self._cells))

    def get_coords(self):
        if self._x is None:
            return (None, None),

        width = self._length if self._tp == 1 else 1
        height = self._length if self._tp == 2 else 1
        decks = tuple((x, y) for x in range(self._x, self._x+width) for y in range(self._y, self._y+height))
        return decks


class GamePole:
    """Class for describing the playing field"""
    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        self.__create_ships()
        self.__place_ships()

    def __create_ships(self):
        self._ships = [Ship(length=i, tp=randint(1, 2)) for i in range(1, 5) for j in range(5-i)]
        self._ships.reverse()

    def __place_ships(self):
        for ship in self._ships:
            other_ships = self._ships.copy()
            other_ships.remove(ship)

            ship.set_start_coords(*[randint(0, self._size-1) for i in range(2)])
            while ship.is_out_pole(self._size) or any(map(ship.is_collide, other_ships)):
                ship.set_start_coords(*[randint(0, self._size-1) for i in range(2)])

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            if ship.is_move:
                other_ships = self._ships.copy()
                other_ships.remove(ship)

                sailing = choice((1, -1))
                ship.move(sailing)
                if ship.is_out_pole(self._size) or any(map(ship.is_collide, other_ships)):
                    ship.move(-2 * sailing)
                if ship.is_out_pole(self._size) or any(map(ship.is_collide, other_ships)):
                    ship.move(sailing)

    def show(self, is_open=True, shooting_area=None):
        if is_open:
            for row in self.get_pole():
                print(*row)
        else:
            for i, row in enumerate(self.get_pole()):
                for j, n in enumerate(row):
                    if n != 2:
                        n = '*' if (i, j) not in shooting_area else 0
                    print(n, end=' ')
                print()

    def get_pole(self):
        pole = [[0] * self._size for i in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            for i, n in enumerate(ship.cells):
                if ship.tp == 1:
                    pole[x+i][y] = n
                elif ship.tp == 2:
                    pole[x][y+i] = n

        return pole

    @property
    def size(self):
        return self._size


class Player:
    """Parent class for computer and human players"""
    def __init__(self, pole_size):
        self._pole = GamePole(pole_size)
        self._pole.init()

        self._enemy_pole = None
        self._shooting_area = [(x, y) for x in range(pole_size) for y in range(pole_size)]
        self._hited_ship = None

    def set_enemy(self, enemy):
        if not isinstance(enemy, self.__class__.__mro__[-2]):
            raise ValueError("Enemy must be Player (Person or Computer)")
        self._enemy_pole = enemy._pole

    def make_turn(self):
        raise NotImplementedError

    def _chose_coords(self):
        raise NotImplementedError

    def _get_hited_ship(self, hit_coords):
        for ship in self._enemy_pole.get_ships():
            if hit_coords in ship.get_coords():
                return ship

    def _register_dead_ship(self):
        for cell in self._hited_ship.area:
            if cell in self._shooting_area:
                self._shooting_area.remove(cell)
        self._hited_ship = None

    def show_pole(self):
        self._pole.show()

    def show_enemy_pole(self):
        self._enemy_pole.show(is_open=False, shooting_area=self._shooting_area)

    def get_ships(self):
        return self._pole.get_ships()

    def move_ships(self):
        self._pole.move_ships()

    def hit_ship(self, x, y):
        if self._hited_ship is None or (x, y) not in self._hited_ship.get_coords():
            self._hited_ship = self._get_hited_ship((x, y))
            self._hited_ship.is_move = False

        self._hited_ship[self._hited_ship.get_coords().index((x, y))] += 1


class Computer(Player):
    """Class representing computer player"""
    def __init__(self, pole_size):
        super().__init__(pole_size)
        self._targeting_cells = list()
        self._hited_ship_cells = list()

    def make_turn(self):
        x, y = self._chose_coords()
        print(f"Enemy shoted at {x} {y}!")
        sleep(1)
        if self._enemy_pole.get_pole()[x][y] == 1:
            self._hited_ship_cells.append((x, y))
            self.hit_ship(x, y)

            if self._hited_ship.is_alive:
                self._update_target_cells(x, y)
                print("Our ship was hited!")
            else:
                self._register_dead_ship()
                print("Our ship has sunk!")

        else:
            if (x, y) in self._targeting_cells:
                self._shooting_area.remove((x, y))
                self._targeting_cells.remove((x, y))
            print("The enemy missed.")
        sleep(1)

    def _chose_coords(self):
        target_cells = self._shooting_area if self._hited_ship is None else self._targeting_cells
        return choice(target_cells)

    def _update_target_cells(self, x, y):
        if self._hited_ship.cells.count(2) == 1:
            self._targeting_cells = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        else:
            if self._hited_ship.tp == 1:
                x_max = max(map(lambda t: t[0], self._hited_ship_cells))
                x_min = min(map(lambda t: t[0], self._hited_ship_cells))
                y = self._hited_ship_cells[0][1]

                self._targeting_cells = [(x_max + 1, y), (x_min - 1, y)]

            elif self._hited_ship.tp == 2:
                y_max = max(map(lambda t: t[1], self._hited_ship_cells))
                y_min = min(map(lambda t: t[1], self._hited_ship_cells))
                x = self._hited_ship_cells[0][0]

                self._targeting_cells = [(x, y_max + 1), (x, y_min - 1)]

        self._targeting_cells = list(filter(lambda t: t in self._shooting_area, self._targeting_cells))

    def _register_dead_ship(self):
        super()._register_dead_ship()
        self._targeting_cells.clear()
        self._hited_ship_cells.clear()


class Person(Player):
    """Class for human player"""
    def make_turn(self):
        x, y = self._chose_coords()
        if self._enemy_pole.get_pole()[x][y] == 1:
            self.hit_ship(x, y)

            if self._hited_ship.is_alive:
                print("Hited!")
            else:
                self._register_dead_ship()
                print("The ship was successfully sunk.")

        else:
            print("Miss shooted!")
        sleep(1)

    def _chose_coords(self):
        while True:
            try:
                x, y = map(int, input("Where to shoot?\n").split())
                if not 0 <= x < self._pole.size or not 0 <= y < self._pole.size:
                    raise ValueError("Coordinates must be positive integers no more then game pole")
            except:
                print("Wrong coordinates. Try again.")
            else:
                return x, y


class SeaBattle:
    """Gameplay class"""
    GAME_POLE_SIZE = 10
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        self.computer = Computer(self.GAME_POLE_SIZE)
        self.player = Person(self.GAME_POLE_SIZE)

        self.computer.set_enemy(self.player)
        self.player.set_enemy(self.computer)

    def gameplay(self):
        print(dedent("""\
        Greetings.
        This is a sea battle game. In order to make a shot, wait for your turn and enter the coordinates separated by a space.
        The result will be displayed in the form of a report and a map of the opponent's field.
        The computer will also make shots, the results will be displayed on the map of your field.
        If all your ships sink before the enemy ships, you lose.
        Good luck chomander!"""))
        sleep(5)
        print()

        while True:
            print("It's your turn!")
            self.player.show_enemy_pole()
            self.player.make_turn()
            if self.__player_wins():
                break
            self.player.move_ships()
            self.computer.make_turn()
            self.player.show_pole()
            if self.__computer_wins():
                break
            self.computer.move_ships()

        if self.__player_wins():
            print("You win!")
        else:
            print("You lose. Maybe another time.")

    def __player_wins(self):
        return all(map(lambda ship: not ship.is_alive, self.computer.get_ships()))

    def __computer_wins(self):
        return all(map(lambda ship: not ship.is_alive, self.player.get_ships()))


game = SeaBattle()
game.gameplay()