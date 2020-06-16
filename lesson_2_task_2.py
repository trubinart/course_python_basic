
list = input('Введите список пожалуйста через запятую: ').split(',')
list_2 = list[:]

i_1 = 0
i_2 = 1
len_list = len(list)

while i_2 < len_list:
    list_2[i_1] = list[i_2]
    list_2[i_2] = list[i_1]
    i_1 +=2
    i_2 +=2

print(list_2)
print(type(list_2[1]))