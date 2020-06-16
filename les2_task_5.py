while True:
     userAsk = input('Введите число для рейтинга: ')
     if userAsk.isdigit():
         userAsk = int(userAsk)
         break
     else:
         print('Ты что дурачок, написано же, введи число.')

list = [7, 8, 9, 11, 22]
list.append(userAsk)
list.sort()
list.reverse()
result = ''
len = int(len(list))
i=0

while i < len:
    for num in list:
        if i < (len-1):
            result += str(num) + ', '
            i += 1
        else:
            result += str(num)
            i += 1
print(f'Рейтинг {result}')
