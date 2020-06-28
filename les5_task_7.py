import json

avarage_list = []
profit_list = []
with open('file_for_task_7.txt', 'r', encoding= 'UTF-8') as file:
    for firm in file:
        firm = firm.replace('.', '')
        firm_list = firm.split()
        firm_name = firm_list[0]
        firm_fin_result = int(firm_list[2]) - int(firm_list[3])
        if firm_fin_result > 0:
            print(f'Фирма {firm_name} получила прибыль в размере {firm_fin_result}')
            avarage_list.append(firm_fin_result)
            profit_dict = {}
            profit_dict[firm_name] = firm_fin_result
            profit_list.append(profit_dict)
        else:
            print(f'Фирма {firm_name} получила убыток в размере {firm_fin_result}')
            profit_dict = {}
            profit_dict[firm_name] = firm_fin_result
            profit_list.append(profit_dict)

avarage_profit = sum(avarage_list) / len(avarage_list)
profit_dict = {}
profit_dict['avarage_profit'] = avarage_profit
profit_list.append(profit_dict)
print(f'Средняя прибыль среди команий с положительной прибылью составила {avarage_profit}')
print(f'Финальный список со словарями {profit_list}')

with open('file_for_task_7.json', 'w', encoding= 'UTF-8') as json_file:
    json.dump(profit_list, json_file)

