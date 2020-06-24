from functools import reduce

# def factotial(num):
#     if num == 0:
#         return 1
#     else:
#         return factotial(num - 1) * num

def multiply(previous_num, next_num):
    return previous_num * next_num

def factotorial(num):
    list_factorial = []
    i = 1
    while i <= num:
        for i in range(i, num + 1):
            list_factorial.append(i)
            factorial_value = reduce(multiply, list_factorial)
            i +=1
            yield factorial_value

for i in factotorial(7):
    print(i)