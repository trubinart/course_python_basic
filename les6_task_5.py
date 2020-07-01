class Stationery:
    def __init__(self, title):
        self.name = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print('Рисуем РУЧКОЙ')

class Pencil(Stationery):
    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print('Рисуем КАРАНДАШОМ')

class Handle(Stationery):
    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print('Рисуем МАРКЕРОМ')

a = Pen()
print(a.name)
a.draw()

b = Pencil()
print(b.name)
b.draw()

c = Handle()
print(c.name)
c.draw()