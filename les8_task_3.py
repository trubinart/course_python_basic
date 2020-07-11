
class NotTextError(Exception):
    def __init__(self, text):
        self.text = text

result_list = []

while True:
    user_ask = input('Введите число для добавления в список (для выхода введите "stop"): ')
    if user_ask == 'stop':
        print(f'Ваш список {result_list}')
        break
    else:
        try:
            user_ask_type = user_ask.isdigit()
            if user_ask_type:
                user_ask = user_ask
                result_list.append(int(user_ask))
            else:
                raise NotTextError('Вы ввели текст, а надо число!')
        except NotTextError as err:
            print(err)
            continue