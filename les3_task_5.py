
#Function for getting sum number of input
def sum_list(list:str) -> int:
    finish_sum = 0
    for i in range(0, len(user_ask)):
        num = int(user_ask[i])
        finish_sum += num
    return finish_sum

#Realizing program from home task
user_ask = input('Введите числа через пробел:')
result = 0
while True:
    if user_ask != 'end':
        user_ask = user_ask.split()
        middle_result = sum_list(user_ask)
        result = result + middle_result
        print(f'Сумма ваших чисел {result}')
        user_ask = input('Введите еще числа (оставноить программу "end"):')
    else:
        print(f'Программа завершена, ваша сумма {result}')
        break