
class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        def get_line(list_name):
            list = []
            for x in list_name:
                a = f'    {x}'
                list.append(a)
            list.append('\n')
            ''.join(list)
            return ''.join(list)

        list_matrix = []
        for i in self.matrix:
            list_matrix.append(get_line(i))
        return ''.join(list_matrix)


    def __add__(self, other):
        matrix3 = []
        num_list = 0
        for list in self.matrix:
            result = []
            for i in list:
                sum_element = i + other.matrix[num_list][list.index(i)]
                result.append(sum_element)
            matrix3.append(result)
            num_list += 1
        print(matrix3)


matrix1 = [[1, 2, 3, 5, 6], [1, 2, 3, 5, 6]]
matrix2 = [[11, 21, 31, 51, 61], [12, 22, 32, 52, 62]]

a = Matrix([[1, 2, 3, 5, 6], [1, 2, 3, 5, 6]])
b = Matrix([[11, 21, 31, 51, 61], [12, 22, 32, 52, 62]])
print(a.matrix)
print(b.matrix)
print(a)
print(b)
