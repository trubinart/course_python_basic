from functools import reduce

def multiply(previous_num,second_num):
    return previous_num * second_num

list = [i for i in range(100, 1001) if i%2 == 0]

print(list)
print(reduce(multiply, list))
