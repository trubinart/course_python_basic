# ЗАДАНИЕ 1
my_var_1 = 1
my_var_2 = 2
print(my_var_1, my_var_2)

var_from_user_num = input('Введите число: ')
var_from_user_str = input('Введите текст: ')

var_from_user_num = int(var_from_user_num)

print(var_from_user_num)
print(var_from_user_num)
print(var_from_user_str)

# ЗАДАНИЕ 2
user_ask_time = input('Введите число в секундах: ')
while True:
    if user_ask_time.isdigit():
        user_ask_time = int(user_ask_time)
        how_min_in_user_ask = int(user_ask_time / 60)
        user_hour = int(how_min_in_user_ask // 60)
        user_min = int(how_min_in_user_ask % 60)
        user_sec = user_ask_time % 60
        print(f'{user_hour} часов {user_min} минут {user_sec} секунд')
        break
    else:
        user_ask_time = input('Вы ввели текст, а нужны секунды: ')
