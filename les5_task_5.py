from random import randint

with open('file_for_task_5.txt', 'w', encoding= 'UTF-8') as file:
    sum = 0
    for i in range(1, 100):
        num = randint(0, 1000)
        sum = sum + num
        file.write(f'{num} ')
    print(f'Сумма всех чисел в файле {sum}')