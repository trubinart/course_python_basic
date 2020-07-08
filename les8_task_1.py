class Data:

    def __init__(self, data):
        self.data = data
        print(self.data)
        print(Data.change_data(data))
        print(Data.validation(data))

    @classmethod
    def change_data(cls, data):
        data_list = list(map(int, data.split('-')))
        return data_list

    @staticmethod
    def validation(data):
        data_list = list(map(int, data.split('-')))
        day_in_febrary = 29 if not data_list[2] % 4 else 28
        day_in_month = {'1': 30, '2': day_in_febrary, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30,
                        '10': 31, '11': 30, '12': 31}
        year = f'Год {data_list[2]} введен верно' if data_list[2] > 1000 else 'Год введен не верно'
        month = f'Месяц {data_list[1]} введен верно' if 0 < data_list[1] <= 12 else 'Месяц введен не верно'

        try:
            day = f'День {data_list[0]} введен верно' if 0 < data_list[0] <= day_in_month[
                f'{data_list[1]}'] else 'День введен не верно'
        except KeyError:
            day = f'День {data_list[0]} введен верно' if 0 < data_list[0] <= 31 else 'День введен не верно'

        return f'{year} \n {month} \n  {day}'

a = Data('30-02-2020')
