while True:
     userAsk = input('Введите номер месяца года: ')
     if userAsk.isdigit():
         userAsk = int(userAsk)
         if userAsk < 12 > 0 and userAsk != 0:
             userAsk = str(userAsk)
             break
         else:
             print('Номер месяца должен быть от 1 до 12')
     else:
         print('Месяц года должен быть числом от 1 до 12')

list = [
        {'12':'Зима'},
        {'1':'Зима'},
        {'2':'Зима'},
        {'3':'Весна'},
        {'4':'Весна'},
        {'5':'Весна'},
        {'6':'Лето'},
        {'7':'Лето'},
        {'8':'Лето'},
        {'9':'Осень'},
        {'10':'Осень'},
        {'11':'Осень'}
        ]

i = 0
while i < 12:
    for key in list[i].keys():
        if key == userAsk:
            print(f'Это время года: {list[i].get(key).lower()}')
            break
    i +=1