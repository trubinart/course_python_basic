class Road:
    def __init__(self, length:int, width:int):
        self._length = length
        self._width = width

    def count_weight_asphalt(self):
        result = self._length * self._width * 25 * 5
        result_tonn = result / 1000
        print(f'Для покрытия дороги в {self._length} метров, шириной {self._width} метров нужно {result} кг'
              f' или {result_tonn} тонн асфальта')

a = Road(20,5000)
a.count_weight_asphalt()