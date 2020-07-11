class PlaceError(Exception):
    def __init__(self, text):
        self.text = text

class WareHouse:
    __all_place_count = 1000  #всего места на складе
    _free_place_count = 3  #свободное на складе #должно стоять 1000, но стоит три, чтобы проверить отработку исключения
                            #когда склад заполнен
    _office_equipment_dict = {}

    @classmethod
    def show_all_place_count(cls):
        return cls.__all_place_count

class OfficeEquipment:
    def __init__(self, take_place: int, price : float, prioritet_index: int):
        self.take_plase = take_place  #сколько места занимает
        self.price = price  #цена
        self.need_prioritet = prioritet_index  #индекс необходимости компании

    def check_arguments(func):
        def wrap(*args):
            type_1 = type(args[1])
            type_2 = type(args[2])
            if type_1 == str and type_2 == int:
                result = func(*args)
                return result
            else:
                print('Один из аргументов не верный! Первый должен быть текстом, второй числом!')
        return wrap

    @check_arguments
    def add_equipment(self, office_direct, count=0):
        check_free_place = count * self.take_plase
        try:
            if WareHouse._free_place_count == 0:
                print(f'Склад заполнен полностью!')

            elif WareHouse._free_place_count >= check_free_place:
                try:
                    WareHouse._office_equipment_dict[office_direct]
                except KeyError:
                    WareHouse._office_equipment_dict[office_direct] = {}

                try:
                    i = WareHouse._office_equipment_dict[office_direct][self.__class__.__name__]
                except KeyError:
                    i = 0
                WareHouse._office_equipment_dict[office_direct][self.__class__.__name__] = i + count
                WareHouse._free_place_count -= i + (count * self.take_plase)
            else:
                raise PlaceError(f'Место на складе не хватает, осталось всего {WareHouse._free_place_count} мест, '
                                 f'а вы хотите добавить {count} {self.__class__.__name__}'
                                 f', которые занимают {count * self.take_plase} мест.')
        except PlaceError as err:
            print(err)

class Printer(OfficeEquipment):
    def __init__(self, take_place: int, price: float, prioritet_index: int, print_list: int):
        self.print_list = print_list  #количество листов, ПЕЧАТАЕМЫХ в минуту
        super().__init__(take_place, price, prioritet_index)

class Scaner (OfficeEquipment):
    def __init__(self, take_place: int, price: float, prioritet_index: int, scaner_list: int):
        self.scaner_list = scaner_list #количество листов, СКАНИРУЕМЫХ в минуту
        super().__init__(take_place, price, prioritet_index)

class Xerox (OfficeEquipment):
    def __init__(self, take_place: int, price: float, prioritet_index: int, xerox_list: int):
        self.xerox_list = xerox_list #количество листов, КСЕРОКОПИРУЕМЫХ в минуту
        super().__init__(take_place, price, prioritet_index)


b = Printer(1, 543.50, 1, 140)
b.add_equipment('Marketing', 1)
print(WareHouse._office_equipment_dict)
print(WareHouse._free_place_count)

d = Scaner(1, 1900.00, 1, 140)
d.add_equipment('Marketing', 1)
print(WareHouse._office_equipment_dict)
print(WareHouse._free_place_count)

c = Xerox(1, 1900.00, 1, 140)
c.add_equipment('Sales', 1)
print(WareHouse._office_equipment_dict)
print(WareHouse._free_place_count)

#проверка что склад заполнен полностью
# e = Xerox(1, 1900.00, 1, 140)
# e.add_equipment('Marketing', 1)

#проверка ошибки ввода
# c = Xerox(1, 1900.00, 1, 140)
# c.add_equipment('Sales', 'RaiseError')



