class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повренула на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышен лимит скорости в 60 км')
        else:
            print(f'Скорость автомобиля {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышен лимит скорости в 40 км')
        else:
            print(f'Скорость автомобиля {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

(60, 'white', 'KIA', 'False')
(150, 'red', 'AUDI', 'False')
(60, 'black', 'VAZ', 'False')
(100, 'black', 'RENO', 'True')

print('TownCar')
a = TownCar(60, 'white', 'KIA', 'False')
print(a.name)
print(a.color)
print(a.is_police)
a.go()
a.show_speed()
a.turn('право')
a.stop()

print('\nSportCar')
b = SportCar(150, 'red', 'AUDI', 'False')
print(b.name)
print(b.color)
print(b.is_police)
b.go()
b.show_speed()
b.turn('лево')
b.stop()

print('\nWorkCar')
c = WorkCar(60, 'black', 'VAZ', 'False')
print(c.name)
print(c.color)
print(c.is_police)
c.go()
c.turn('лево')
c.show_speed()
c.stop()

print('\nPoliceCar')
d = PoliceCar(100, 'black', 'RENO', 'True')
print(d.name)
print(d.color)
print(d.is_police)
d.go()
d.show_speed()
d.turn('лево')
d.stop()
