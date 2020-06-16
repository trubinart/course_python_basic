
userAsk  = input('Введите несколько слов, разделенные пробелами: ')
list = userAsk.split()

for int, el in enumerate(list):
    if len(el) >= 10:
        print(int, el[:10])
    else:
        print(int, el)