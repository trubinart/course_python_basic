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
        hour = user_ask_time // 3600
        min = int(user_ask_time % 3600 /60)
        sec = user_ask_time % 60
        print(f'{hour} час : {min} мин : {sec} сек')
        break
    else:
        user_ask_time = input('Вы ввели текст, а нужны секунды: ')

# ЗАДАНИЕ 3
user_ask_number = input('Введите любое число: ')
while True:
    if user_ask_number.isdigit():
        sum = int(user_ask_number) + int(user_ask_number*2) + int(user_ask_number*3)
        print(sum)
        break
    else:
        user_ask_number = input('Вы ввели текст, а нужны цифры: ')


# ЗАДАНИЕ 4
division = 1
counter = 1
remains = 0

while True:
    user_ask_number = input('Введите любое число: ')
    if user_ask_number.isdigit():
        user_ask_number = int(user_ask_number)
        while counter != 0:
            counter = int(user_ask_number / division)
            division *= 10
            number = counter % 10
            if number > remains:
                remains = number
        print(f'Самое большая цифра в числе {remains}')
        break
    else:
        user_ask_number = input('Вы ввели текст, а нужны цифры: ')

# ЗАДАНИЕ 5
while True:
    user_ask_revenue = input('Введите прибыль компании: ')
    if user_ask_revenue.isdigit():
        user_ask_revenue = int(user_ask_revenue)
        break
    else:
        print('Прибыль должна быть числом')

while True:
    user_ask_loses = input('Введите издержки компании: ')
    if user_ask_loses.isdigit():
        user_ask_loses = int(user_ask_loses)
        break
    else:
        print('Издержки должны быть числом. Ты что, дурачок)')

profit = user_ask_revenue - user_ask_loses
if profit > 0:
    profitability = int(profit / user_ask_revenue * 100)
    print(f'Компания отработала в прибыль c рентабельностью в {profitability}%')
    employees = input('А сколько сотрудников работает?: ')
    employees = int(employees)
    profit_on_employees = int(profit / employees)
    print(f'Прибыль на одного сотрудника составила {profit_on_employees}$. Ты просто красавчик!')
else:
    print('Фирам отработала в минус. Вам надо прекратить заниматься бизнесом!')

# ЗАДАНИЕ 6
while True:
    a = input('Введите результат в первый день: ')
    if a.isdigit():
        a = int(a)
        break
    else:
        print('Результат первого дня должно быть числом!')

while True:
    b = input('К чему стремимся: ')
    if b.isdigit():
        b = int(b)
        break
    else:
        print('И то, к чему стремимся тоже должно быть числом!')

day = 1
print(f'1-й день: {a}')

while a <= b:
    a = a * 1.1
    day += 1
    print('%d-й день: %.2f' % (day, a))
else:
    print(f'Спортсмен достигнет результата на {day} день')






