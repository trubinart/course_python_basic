class Cell:
    idx = 0

    def __init__(self, mesh_count = 1 ):
        Cell.idx += 1
        self.mesh_count = mesh_count

    def __add__(self, other):
        mesh_count = self.mesh_count + other.mesh_count
        return Cell(mesh_count)

    def __sub__(self, other):
        mesh_count = self.mesh_count - other.mesh_count
        if mesh_count > 0:
            return Cell(mesh_count)
        else:
            raise Exception('Разница меньше нуля. Вычитание не возможно')

    def __mul__(self, other):
        mesh_count = self.mesh_count * other.mesh_count
        return Cell(mesh_count)

    def __truediv__(self, other):
        mesh_count = self.mesh_count // other.mesh_count
        return Cell(mesh_count)

    def make_order(self, line):
        list = []
        whole = self.mesh_count // line
        remains = self.mesh_count % line

        i = 0
        while i < whole:
            line_in_list = ''
            line_in_list = ('*' * line) + '\n'
            list.append(line_in_list)
            i += 1
        else:
            line_in_list = ''
            line_in_list = ('*' * remains) + '\n'
            list.append(line_in_list)
        return ''.join(list)

a = Cell()
b = Cell()
c = a + b
e = c + a
d = e - b
g = e * d
h = g / d

print(a.mesh_count)
print(b.mesh_count)
print(c.mesh_count)
print(e.mesh_count)
print(d.mesh_count)
print(g.mesh_count)
print(h.mesh_count)
print(f'Всего клеток {Cell.idx}')
print(g.make_order(3))

