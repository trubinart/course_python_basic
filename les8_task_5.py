class WareHouse:
    __all_place_count = 1000  #всего места на складе
    _free_place_count = 1000  #свободное на складе
    _office_equipment_dict = {}

    @classmethod
    def show_all_place_count(cls):
        return cls.__all_place_count

class OfficeEquipment:
    def __init__(self, take_place: int, price : float, prioritet_index: int):
        self.take_plase = take_place  #сколько места занимает
        self.price = price  #цена
        self.need_prioritet = prioritet_index  #индекс необходимости компании

    def add_equipment(self, office_direct, count=0):
        try:
            WareHouse._office_equipment_dict[office_direct]
        except KeyError:
            WareHouse._office_equipment_dict[office_direct] = {}

        try:
            i = WareHouse._office_equipment_dict[office_direct][self.__class__.__name__]
        except KeyError:
            i = 0
        WareHouse._office_equipment_dict[office_direct][self.__class__.__name__] = i + count
        WareHouse._free_place_count -= i + (count * self.take_plase )


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


b = Printer(9, 543.50, 1, 140)
b.add_equipment('Marketing', 5)
print(WareHouse._office_equipment_dict)
print(WareHouse._free_place_count)

c = Printer(2, 490.00, 1, 140)
c.add_equipment('Marketing', 5)
print(WareHouse._office_equipment_dict)
print(WareHouse._free_place_count)

d = Scaner(4, 1900.00, 1, 140)
d.add_equipment('Marketing', 6)
print(WareHouse._office_equipment_dict)
print(WareHouse._free_place_count)

print(WareHouse.show_all_place_count())