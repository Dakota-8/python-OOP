def input_int_numbers(string):
    try:
        return [int(i) for i in string.split()]
    except ValueError:
        raise TypeError('все числа должны быть целыми')


while True:
    try:
        print(*input_int_numbers(input()))
        break
    except TypeError:
        continue
