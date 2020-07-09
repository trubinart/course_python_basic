
class ZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text

numerals = input('Введите числитель: ')


while True:
    try:
        numerals = int(numerals)
        break
    except ValueError:
        numerals = input('Нужно число. Введите числитель еще раз: ')

denominator = input('Введите знаменатель: ')

while True:
    try:
        denominator = int(denominator)
        if denominator == 0:
            raise ZeroDivisionError('На ноль делить нельзя!')
        break
    except ValueError:
        denominator = input('Нужно число. Введите знаменатель еще раз: ')
    except ZeroDivisionError as var:
        print(var)
        denominator = input('Введите знаменатель еще раз: ')

print(f'Результат деления {numerals/denominator}')