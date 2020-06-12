# ЗАДАНИЕ 1
# my_var_1 = 1
# my_var_2 = 2
# print(my_var_1, my_var_2)
#
# var_from_user_num = input('Введите число: ')
# var_from_user_str = input('Введите текст: ')
#
# var_from_user_num = int(var_from_user_num)
#
# print(var_from_user_num)
# print(var_from_user_num)
# print(var_from_user_str)

# ЗАДАНИЕ 2
# user_ask_time = input('Введите число в секундах: ')
# while True:
#     if user_ask_time.isdigit():
#         user_ask_time = int(user_ask_time)
#         hour = user_ask_time // 3600
#         min = int(user_ask_time % 3600 /60)
#         sec = user_ask_time % 60
#         print(f'{hour} час : {min} мин : {sec} сек')
#         break
#     else:
#         user_ask_time = input('Вы ввели текст, а нужны секунды: ')

# ЗАДАНИЕ 3
# user_ask_number = input('Введите любое число: ')
# while True:
#     if user_ask_number.isdigit():
#         sum = int(user_ask_number) + int(user_ask_number*2) + int(user_ask_number*3)
#         print(sum)
#         break
#     else:
#         user_ask_number = input('Вы ввели текст, а нужны цифры: ')


# ЗАДАНИЕ 4
# division = 1
# counter = 1
# remains = 0
#
# while True:
#     user_ask_number = input('Введите любое число: ')
#     if user_ask_number.isdigit():
#         user_ask_number = int(user_ask_number)
#         while counter != 0:
#             counter = int(user_ask_number / division)
#             division *= 10
#             number = counter % 10
#             if number > remains:
#                 remains = number
#         print(f'Самое большая цифра в числе {remains}')
#         break
#     else:
#         user_ask_number = input('Вы ввели текст, а нужны цифры: ')



