def find_and_sum_number(line: str) -> int:
    """
    Function find all number in line (number can contain several element) and summarize all number.
    It doesn't depend for gap in line.

    :param line: line with letters and numbers
    :return: sum all number
    """
    line_number = []
    i = 0
    while i < len(line):
        letter = line[i]
        if letter.isdigit():
            s_int = ''
            while letter.isdigit():
                s_int += letter
                i += 1
                letter = line[i]
            line_number.append(int(s_int))
        else:
            i += 1
            continue
    return sum(line_number)

final_dict = {}
with open('file_for_task_6.txt', 'r', encoding= 'UTF-8') as file:
    for i in file:
        line = i
        key_for_dict = line.split()
        final_dict[key_for_dict[0]] = find_and_sum_number(line)
print(final_dict)







