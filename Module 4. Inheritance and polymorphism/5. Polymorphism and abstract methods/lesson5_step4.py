"""
Подвиг 3. В программе объявлены два класса:

class Student:
    def __init__(self, fio, group):
        self._fio = fio  # ФИО студента (строка)
        self._group = group # группа (строка)
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з:
        {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

Первый класс описывает студентов, а второй - менторов. Вам поручается на основе базового класса Mentor разработать еще
два дочерних класса:

Lector - для описания лекторов;
Reviewer - для описания экспертов.

Объекты этих классов должны создаваться командами:

lector = Lector(fio, subject)
reviewer = Reviewer(fio, subject)

где fio - ФИО (строка); subject - предмет (строка). Инициализации этих параметров (fio, subject) должна выполняться
базовым классом Mentor.

В самих классах Lector и Reviewer необходимо объявить метод:

def set_mark(self, student, mark): ...

для простановки оценки (mark) студенту (student). Причем, в классе Lector оценки добавляются в список _lect_marks
объекта класса Student, а в классе Reviewer - в список _house_marks. Используйте для этого методы add_lect_marks() и
add_house_marks() класса Student.

Также в классах Lector и Reviewer должен быть переопределен магический метод:

__str__()

для формирования следующей информации об объектах:

- для объектов класса Lector: Лектор <ФИО>: предмет <предмет>
- для объектов класса Reviewer: Эксперт <ФИО>: предмет <предмет>

Пример использования классов (эти строчки в программе писать не нужно):

lector = Lector("Балакирев С.М.", "Информатика")
reviewer = Reviewer("Гейтс Б.", "Информатика")
students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
persons = [lector, reviewer]
lector.set_mark(students[0], 4)
lector.set_mark(students[1], 2)
reviewer.set_mark(students[0], 5)
reviewer.set_mark(students[1], 3)
for p in persons + students:
    print(p)
# в консоли будет отображено:
# Лектор Балакирев С.М.: предмет Информатика
# Эксперт Гейтс Б.: предмет Информатика
# Студент Иванов А.Б.: оценки на лекциях: [4]; оценки за д/з: [5]
# Студент Гаврилов С.А.: оценки на лекциях: [2]; оценки за д/з: [3]

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
P.P.S. Подумайте, где в этой программе полиморфизм.
"""


class Student:
    def __init__(self, fio, group):
        self._fio = fio  # ФИО студента (строка)
        self._group = group # группа (строка)
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


class Lector(Mentor):
    def set_mark(self, student, mark):
        Student.add_lect_marks(student, mark)

    def __str__(self):
        return f'Лектор {self._fio}: предмет {self._subject}'


class Reviewer(Mentor):
    def set_mark(self, student, mark):
        Student.add_house_marks(student, mark)

    def __str__(self):
        return f'Эксперт {self._fio}: предмет {self._subject}'
