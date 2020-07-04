from abc import ABC, abstractmethod

class Clothes(ABC):
    __all_textile = {}

    def add_textile_dict(self, name, size):
        self.__all_textile[name] = size

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def calculate_textile(self):
        pass

    @property
    def all_textile(self):
        result = 0
        for value in self.__all_textile.values():
            result += value
        return (f'Всего нужно на всю одежду {result:.1f} метров ткани.')

class Coat(Clothes):

    def calculate_textile(self):
        result = (self.size / 6.5) + 0.5
        super().add_textile_dict(self.name, result)
        return f'{result:.1f}'

    def __init__(self, name, size):
        self.name = name
        self.size = size
        super().__init__(name, size)
        self.calculate_textile()

class Suit(Clothes):

    def calculate_textile(self):
        result = (2 * self.size) + 0.3
        super().add_textile_dict(self.name, result)
        return f'{result:.1f}'

    def __init__(self, name, size):
        self.name = name
        self.size = size
        super().__init__(name, size)
        self.calculate_textile()


a = Coat('Педжак крутой', 5)
b = Coat('Красный педжак', 4)
c = Suit('Пальто оборванное', 12)
e = Suit('Желтое пальто', 90)
print(a.name, a.calculate_textile())
print(b.name, b.calculate_textile())
print(c.name, c.calculate_textile())
print(e.name, e.calculate_textile())

print(e.all_textile)


