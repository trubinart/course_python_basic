#Вариант 1
def my_func (x, y):
    y = abs(y)
    return x ** y
print(my_func(2,-2))

#Вариант 2
def my_func_2 (x, y):
    y = abs(y)
    result_2 = 0
    for i in range (0, y):
        result = x * x
        result_2 = result_2 + result
        i += 1
    return result_2
print(my_func_2(2,2))
