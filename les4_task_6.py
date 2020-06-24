#итератор чисел
from itertools import count, cycle

for i in count(1):
    if i > 15:
        break
    else:
        print(i)

#итератор букв
num = 0
for i in cycle('ABCD'):
    if num > 10:
        break
    else:
        print(i)
        num += 1