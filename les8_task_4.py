
class WareHouse:
    __work_time ={
        'понедельник': {'start_time': 9.00, 'close_time': 20.00},
        'вторник': {'start_time': 9.00, 'close_time': 20.00},
        'среда': {'start_time': 9.00, 'close_time': 20.00},
        'четверг': {'start_time': 9.00, 'close_time': 20.00},
        'пятница': {'start_time': 9.00, 'close_time': 20.00},
        'суббота': {'start_time': None, 'close_time': None},
        'воскресенье': {'start_time': None, 'close_time': None}
    }
    __all_place_count = 100  #всего места на складе
    __free_place_count = 100  #свободное на складе

class OfficeEquipment:
    def __init__(self, take_place: int, price : float, prioritet_index: int):
        self.take_plase = take_place  #сколько места занимает
        self.price = price  #цена
        self.need_prioritet = prioritet_index  #индекс необходимости компании

class Printer(OfficeEquipment):
    def __init__(self, take_place: int, price : float, prioritet_index: int, print_list: int):
        self.print_list = print_list  #количество листов, ПЕЧАТАЕМЫХ в минуту
        super().__init__(take_place, price, prioritet_index)

class Scaner (OfficeEquipment):
    def __init__(self, take_place: int, price : float, prioritet_index: int, scaner_list: int):
        self.scaner_list = scaner_list #количество листов, СКАНИРУЕМЫХ в минуту
        super().__init__(take_place, price, prioritet_index)

class Xerox (OfficeEquipment):
    def __init__(self, take_place: int, price : float, prioritet_index: int, xerox_list: int):
        self.xerox_list = xerox_list #количество листов, КСЕРОКОПИРУЕМЫХ в минуту
        super().__init__(take_place, price, prioritet_index)


b = Printer(3, 543.50, 1, 140)
print(1)