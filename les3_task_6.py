def text_function(word: str):
    return word.title()

user_ask = input('Введите текст латинских слов в нижнем регистре: ')
user_ask_list = user_ask.split()
result = ''
for i in range(0, len(user_ask_list)):
    middle_result = text_function(user_ask_list[i])
    result = result + middle_result + ' '
print(result.rstrip())
