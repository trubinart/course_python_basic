import time

def time_timer(sec_gap:int) -> float:
    """
    Function take time gap in seconds and give timer from time now to time + gap in seconds.
    :param sec_gap: int
    :return: float
    """
    time_now = time.time()
    gap_1 = sec_gap
    time_gap = time_now + gap_1
    while True:
        time_cycle = time.time()
        if time_cycle == time_gap:
            break

class TrafficLight:
    __color1 = 'Красный'
    __color2 = 'Оранжевый'
    __color3 = 'Зеленый'

    def change_trafficLight(self):
        check_trafficLight = (self.__color1, self.__color2, self.__color3)
        check_list = []
        print(self.__color1)
        check_list.append(self.__color1)
        time_timer(7)
        print(self.__color2)
        check_list.append(self.__color2)
        time_timer(2)
        print(self.__color3)
        check_list.append(self.__color3)
        time_timer(1)
        check_list = tuple(check_list)
        if check_list == check_trafficLight:
            print('Светофор выключился')
        else:
            print('Ошибка, режим светофора сбился')

a = TrafficLight()
a.change_trafficLight()