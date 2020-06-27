
with open('file_for_task_2.txt', 'r', encoding='UTF-8') as file:
    num = 1
    for i in file:
        list = i.split()
        result = len(list)
        print(f'В строке {num} - {result} слов')
        num += 1

with open('file_for_task_2.txt', 'r', encoding='UTF-8') as file:
    count_line = len(file.readlines())
    print(f'В файле всего {count_line} строк')
