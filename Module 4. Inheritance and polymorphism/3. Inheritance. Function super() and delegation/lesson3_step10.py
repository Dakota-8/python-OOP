class StringDigit(str):
    def __init__(self, string):
        self.__check_value(string)
        super().__init__()

    def __check_value(self, other):
        if not all(i.isdigit() for i in other):
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self.__check_value(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        self.__check_value(other)
        return StringDigit(other) + self
