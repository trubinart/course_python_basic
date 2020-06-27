
user_ask = input('Введите строку для записи в файл: ')
with open('file_task_1.txt', 'x', encoding='UTF-8') as file:
    file.write(f'{user_ask}\n')

while user_ask:
    user_ask = input('Может хотите еще что-то записать?: ')
    with open('file_task_1.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{user_ask}\n')
else:
    print('Круто, файл создан и вы можете его прочитать!')
