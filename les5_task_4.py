dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('file_for_task_4.txt', 'r', encoding='UTF-8') as file:
    with open('file_finish_for_task_4.txt', 'x', encoding='UTF-8') as finish_file:
        for num in file:
            line = num
            for key, value in dict.items():
                if line.find(key) == 0:
                    result = line.replace(key, value)
                    finish_file.write(result)