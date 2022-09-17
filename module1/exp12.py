# Тема 8: “Словари”
# 1
import math

data = [{'interface': 'Ethernet0', 'ip': '1.1.1.1', 'status': 'up'},
        {'interface': 'Ethernet1', 'ip': '2.2.2.2', 'status': 'down'},
        {'interface': 'Serial0', 'ip': '3.3.3.3', 'status': 'up'},
        {'interface': 'Serial1', 'ip': '4.4.4.4', 'status': 'up'}]
print('Количество интерфейсов:', len(data))
print('Второй интерфейс:', data[1].values())
print('Статус:', data[3]['status'])
print(data[0].setdefault('notes', 'need to reset'))
data.append({'interface': 'Ethernet2', 'ip': data[2]['ip'], 'status': 'down'})
data[2]['ip'] = '3.3.3.4'
print(data[0].pop('notes'))
data[3]['status'] = 'down'
del data[3]
print(data)
print()

# 2
basket = {'smart watch': 550, 'phone': 1000, 'playstation': 500, 'laptop': 1550, 'music player': 600, 'tablet': 400}
values = basket.values()
print('Total sum:', sum(values))
keys = basket.keys()
print('Good names:', sorted(keys))
print('Good names:', sorted(keys, reverse=True))
basket['music player'] = int(basket['music player'] - (basket['music player'] * 50 / 100))
sell_goods = (5 * basket['phone']) + (3 * basket['laptop'])
count_selling_tablet = math.ceil(sell_goods / basket['tablet'])
print(count_selling_tablet)
basket.update({'iphone': 1300, 'music player': 850, 'headphones': 200})
print(basket)
