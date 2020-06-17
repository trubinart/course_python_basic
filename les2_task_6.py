final_product_list = []
num_product = 0
price_desire = 'да'
while price_desire == 'да':
    userAsk_name = input('Введите название товара: ')

    while True:
        userAsk_price = input('Введите цену товара: ')
        if '.' in userAsk_price:
            i_1 = userAsk_price.split('.')
            i_2 = i_1[0]
            i_3 = i_1[1]
            if i_2.isdigit() and i_3.isdigit():
                userAsk_price = float(userAsk_price)
                break
            else:
                print('Введите цену натуральным числом или числом с плавающей точкой.')
        else:
            if userAsk_price.isdigit():
                userAsk_price = int(userAsk_price)
                break
            else:
                print('Введите цену натуральным числом или числом с плавающей точкой.')

    while True:
        userAsk_count = input('Введите количество товара на складе: ')
        if userAsk_count.isdigit():
            userAsk_count = int(userAsk_count)
            break
        else:
            print('Введите количество товара на складе натуральным числом.')

    userAsk_unit = input('Введите ед. измерения товара: ')

    while True:
        userAsk_weight = input('Введите вес товара (с плавающей точкой): ')
        if '.' in userAsk_weight:
            i_1 = userAsk_weight.split('.')
            i_2 = i_1[0]
            i_3 = i_1[1]
            if i_2.isdigit() and i_3.isdigit():
                userAsk_weight = float(userAsk_weight)
                break
            else:
                print('Введите вес числом с плавающей точкой. первый')
    num_product +=1
    user_dict = {
                 'Название': userAsk_name,
                 'Цена': userAsk_price,
                 'Количество': userAsk_count,
                 'Единицы': userAsk_unit,
                 'Вес':userAsk_weight
                 }
    user_list = []
    user_list.append(num_product)
    user_list.append(user_dict)
    user_list = tuple(user_list)
    final_product_list.append(user_list)
    price_desire = input('Вы хотите добавить еще один товар? (да / нет): ')

print(final_product_list)

final_analysis_dict = {}
num_tuple = 0
count_tupple_in_list = 0
len_tupple_in_list = len(final_product_list)

analysis_list = []
while num_tuple < len_tupple_in_list:
    get_value = final_product_list[num_tuple][1].get('Название')
    analysis_list.append(get_value)
    num_tuple += 1
final_analysis_dict['Название'] = analysis_list

num_tuple = 0
analysis_list = []
while num_tuple < len_tupple_in_list:
    get_value = final_product_list[num_tuple][1].get('Цена')
    analysis_list.append(get_value)
    num_tuple += 1
final_analysis_dict['Цена'] = analysis_list

num_tuple = 0
analysis_list = []
while num_tuple < len_tupple_in_list:
    get_value = final_product_list[num_tuple][1].get('Количество')
    analysis_list.append(get_value)
    num_tuple += 1
final_analysis_dict['Количество'] = analysis_list

num_tuple = 0
analysis_list = []
while num_tuple < len_tupple_in_list:
    get_value = final_product_list[num_tuple][1].get('Единицы')
    analysis_list.append(get_value)
    num_tuple += 1
final_analysis_dict['Единицы'] = analysis_list

num_tuple = 0
analysis_list = []
while num_tuple < len_tupple_in_list:
    get_value = final_product_list[num_tuple][1].get('Единицы')
    analysis_list.append(get_value)
    num_tuple += 1
final_analysis_dict['Единицы'] = analysis_list

print(final_analysis_dict)

