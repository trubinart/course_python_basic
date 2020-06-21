
def my_func(number_1: int, number_2: int, number_3: int):
    if number_1 == number_2 == number_3:
        return 'Введите разные числа в функцию'
    else:
        number_list = [number_1, number_2, number_3]
        number_list.sort()
        return number_list[-1] + number_list[-2]

print(my_func(90, 10, 10))
