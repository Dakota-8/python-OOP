"""
Подвиг 5. Объявите в программе класс-исключение с именем PrimaryKeyError, унаследованным от базового класса Exception.
Объекты класса PrimaryKeyError должны создаваться командами:

e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо

В первом варианте команды должно формироваться сообщение об ошибке "Первичный ключ должен быть целым неотрицательным
числом". При втором варианте:

"Значение первичного ключа id = <id> недопустимо"

И при третьем:

"Значение первичного ключа pk = <pk> недопустимо"

Эти сообщения должны формироваться при отображении объектов класса PrimaryKeyError, например:

print(e2) # Значение первичного ключа id = abc недопустимо

Затем, сгенерируйте это исключение с аргументом id = -10.5, обработайте его и отобразите на экране объект исключения.

Sample Input:


Sample Output:

Значение первичного ключа id = -10.5 недопустимо


"""


class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if 'id' not in kwargs and 'pk' not in kwargs:
            self.message = 'Первичный ключ должен быть целым неотрицательным числом'
        else:
            key, value = tuple(kwargs.items())[0]
            self.message = f'Значение первичного ключа {key} = {value} недопустимо'

    def __str__(self):
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
