class PhoneBook:
    def __init__(self):
        self.phonebook = []

    def add_phone(self, phone):
        self.phonebook.append(phone)

    def remove_phone(self, indx):
        self.phonebook.pop(indx)

    def get_phone_list(self):
        return self.phonebook


class PhoneNumber:
    def __init__(self, number, full_name):
        self.number = number
        self.fio = full_name


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

print(phones)