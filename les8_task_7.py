class ComplexNumbres:
    def __init__(self, number1, number2):
        self.number = complex(number1, number2)

    def __add__(self, other):
        real_part = self.number.real + other.number.real
        imag_part = self.number.imag + other.number.imag
        return complex(real_part, imag_part)

    def __mul__(self, other):
        real_part = (self.number.real * other.number.real) - (self.number.imag * other.number.imag)
        imag_part = (self.number.real * other.number.imag) + (self.number.imag * other.number.real)
        return complex(real_part, imag_part)


a = ComplexNumbres(1, 2)
print(a.number)

b = ComplexNumbres(1, 2)
print(b.number)

print(a + b)
print(a * b)
