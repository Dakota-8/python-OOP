"""
Подвиг 5. Вы начинаете разрабатывать свой сервис по тестированию. Для этого вам поручается разработать базовый класс
Test для всех видов тестов, объекты которого создаются командой:

test = Test(descr)

где descr - формулировка теста (строка). Если длина строки descr меньше 10 или больше 10 000 символов, то генерировать
исключение командой:

raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

В самом классе Test должен быть объявлен абстрактный метод:

def run(self): ...

который должен быть переопределен в дочернем классе. Если это не так, то должно генерироваться исключение командой:

raise NotImplementedError

Далее, объявите дочерний класс с именем TestAnsDigit для тестирования правильного введенного числового ответа на вопрос
теста. Объекты класса TestAnsDigit должны создаваться командой:

test_d = TestAnsDigit(descr, ans_digit, max_error_digit)

где ans_digit - верный числовой ответ на тест; max_error_digit - максимальная погрешность в указании числового ответа
(необходимо для проверки корректности вещественных чисел, по умолчанию принимает значение 0.01).

Если аргумент ans_digit или max_error_digit не число (также проверить, что max_error_digit больше или равно нулю), то
генерировать исключение командой:

raise ValueError('недопустимые значения аргументов теста')

В классе TestAnsDigit переопределите метод:

def run(self): ...

который должен читать строку из входного потока (ответ пользователя) командой:

ans = float(input()) # именно такой командой, ее прописывайте в методе run()

и возвращать булево значение True, если введенный числовой ответ ans принадлежит диапазону [ans_digit-max_error_digit;
ans_digit+max_error_digit]. Иначе возвращается булево значение False.

Теперь нужно воспользоваться классом TestAnsDigit. Для этого в программе вначале читается сам тест с помощью команд:

descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

Далее, вам необходимо создать объект класса TestAnsDigit с аргументами descr, ans, а аргумент max_error_digit должен
принимать значение по умолчанию 0.01.

Запустите тест командой run() и выведите на экран результат его работы (значение True или False). Если в процессе
создания объекта класса TestAnsDigit или в процессе работы метода run() возникли исключения, то они должны быть
обработаны и на экран выведено сообщение, содержащееся в исключении.

Sample Input:

Какое значение получим, при выполнении команды int(5.7)? | 5
6

Sample Output:

False
"""
from abc import ABC, abstractmethod


class Test(ABC):
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    @abstractmethod
    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.1):
        if type(ans_digit) not in (int, float) or type(max_error_digit) not in (int, float) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))
ans = float(ans)
try:
    test_d = TestAnsDigit(descr, ans)
    res = test_d.run()
    print(res)
except ValueError as e:
    print(e)
