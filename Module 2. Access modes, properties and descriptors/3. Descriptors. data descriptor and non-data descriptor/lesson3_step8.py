"""Подвиг 7. Объявите класс ValidateString для проверки корректности переданной строки. Объекты этого класса создаются
командой:

validate = ValidateString(min_length=3, max_length=100)

где min_length - минимальное число символов в строке; max_length - максимальное число символов в строке.
В классе ValidateString должен быть реализован метод:

validate(self, string) - возвращает True, если string является строкой (тип str) и длина строки в пределах [min_length;
max_length]. Иначе возвращается False.

Объявите дескриптор данных StringValue для работы со строками, объекты которого создаются командой:

st = StringValue(validator=ValidateString(min_length, max_length))

При каждом присвоении значения объекту st должен вызываться валидатор (объект класса ValidateString) и с помощью метода
validate() проверяться корректность присваиваемых данных. Если данные некорректны, то присвоение не выполняется
(игнорируется).

Объявите класс RegisterForm с тремя объектами дескриптора StringValue:

login = StringValue(...) - для ввода логина;
password = StringValue(...)  - для ввода пароля;
email = StringValue(...)  - для ввода Email.

Объекты класса RegisterForm создаются командой:

form = RegisterForm(логин, пароль, email)

где логин, пароль, email - начальные значения логина, пароля и Email.
В классе RegisterForm также должны быть объявлены методы:

get_fields() - возвращает список из значений полей в порядке [login, password, email];
show() - выводит в консоль многострочную строку в формате:

<form>
Логин: <login>
Пароль: <password>
Email: <email>
</form>

P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно."""


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')
