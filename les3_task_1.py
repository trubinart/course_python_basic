def division():
    while True:
        number_1 = input('Введите числитель: ')
        try:
            number_1 = int(number_1)
            break
        except ValueError:
            print('Ошибка ввода команды')

    while True:
        number_2 = input('Введите знаменатель: ')
        try:
            number_2 = int(number_2)
            break
        except ValueError:
            print('Ошибка ввода команды')
    try:
        print(number_1 / number_2)
    except ZeroDivisionError:
        print('Делить на ноль нельзя')

division()

