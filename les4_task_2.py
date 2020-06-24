
list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_2 = [x for x in list_1[1:] if x > list_1[list_1.index(x)-1]]

print((list_2))
