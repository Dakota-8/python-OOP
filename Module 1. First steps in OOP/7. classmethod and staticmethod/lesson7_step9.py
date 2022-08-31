"""Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах. Этот класс должен
иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True, если номер в верном
формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True, если имя записано
верно и False - в противном случае.

Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами. Например,
SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):

is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

Для проверки допустимых символов в классе должен быть прописан атрибут:

CHARS_FOR_NAME = ascii_lowercase.upper() + digits

Подумайте, как правильнее объявить методы check_card_number и check_name (декораторами @classmethod и @staticmethod)."""


from string import ascii_lowercase


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper()

    @staticmethod
    def check_card_number(number):
        num = number.split('-')
        return all(map(lambda x: x.isdigit() and len(x) == 4, num))

    @classmethod
    def check_name(cls, name):
        if len(name.split()) != 2:
            return False
        first_name, second_name = name.split()
        if set(first_name) < set(cls.CHARS_FOR_NAME) and set(second_name) < set(cls.CHARS_FOR_NAME):
            return True
        return False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number)
