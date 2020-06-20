
user_ask = ['Артем', 'Трубин', '1992', 'Н.Новгород', 'trubinart@gmail.com', '89200273336']

def user_information(first_name: str, second_name: str, born_wear: int, city: str, email: str, tel: str) -> str:
    """Function realize print information about user
    :fuction name: user_information
    :param func: first_name, second_name, born_wear, city, email, tel
    :param data: first_name: str, second_name: str, born_wear: int, city: str, email: str, tel: str
    :return: All arguments of function, which are users information
    """
    print(f'Имя: {first_name}\n'
          f'Фамилия: {second_name}\n'
          f'Год рождения: {born_wear}\n'
          f'Город проживания: {city}\n'
          f'Email: {email}\n'
          f'Телефон: {tel}\n'
          )

user_information('Артем', 'Трубин', 1992, 'Н.Новгород', 'trubinart@gmail.com', '89200273336')
print(user_information.__doc__)
