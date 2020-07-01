class Worker:
        name = ''
        surname = ''
        position = ''
        _income = {'Менеджер': {'wage': 10000, 'bonus': 3000},
                    'ТОП менеджер': {'wage': 20000, 'bonus': 4000},
                    'Директор': {'wage': 30000, 'bonus': 5000}}

class Position(Worker):
    def __init__(self):
        super ().__init__()

    def get_total_name(self):
        return self.name + ' ' + self.surname

    def get_income (self):
        result = self._income[self.position]['wage'] + self._income[self.position]['bonus']
        return result

ilya = Position()
ilya.name = 'Илья'
ilya.surname = 'Гончаров'
ilya.position = 'Менеджер'
print(ilya.get_total_name())
print(ilya.get_income())

artem = Position()
artem.name = 'Артем'
artem.surname = 'Трубин'
artem.position = 'ТОП менеджер'
print(artem.get_total_name())
print(artem.get_income())

grisha = Position()
grisha.name = 'Григорий'
grisha.surname = 'Иванов'
grisha.position = 'Директор'
print(grisha.get_total_name())
print(grisha.get_income())
