
with open('file_for_task_3.txt', 'r', encoding = 'UTF-8') as file:
    dict = {}
    for i in file:
        line = i.split()
        dict[line[0]] = int(line[1])
print(f'Все сотрудники и их заработная плата:')
for key, value in dict.items():
        print(f'{key} {value}')

print(f'\nВсе сотрудники, у кого заработная плата меньше 20 000 рублей:')
for key, value in dict.items():
    if value < 20000:
        print(f'{key} {value}')

average_list = []
for value in dict.values():
    average_list.append(value)

average_num = sum(average_list) / len(average_list)
print(f'\nСредняя заработная плата сотрудников {average_num}')