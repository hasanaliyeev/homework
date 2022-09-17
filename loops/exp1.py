import math

month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']
m = 20
if 0 < m <= 12:
    print(month[m - 1])
else:
    print("Error")

# Temperature Calculator
t = '70C'
index = t[-1]
b = t[:-1].isdecimal()
value = t[:-1]

if (index.lower() == 'f') & b:
    result = str(round((int(value) - 32) * 5 / 9, 2)) + 'C'
elif (index.lower() == 'c') & b:
    result = str(round((int(value) * 9 / 5 + 32), 2)) + 'F'
else:
    result = 'Incorrect input'
print('Result:', result)

# work
a = 11
b = 18
res = a + b
if res in range(15, 21):
    print(20)
else:
    print(res)

# work
a = 1
b = -14
c = 15

D = b ** 2 - (4 * a * c)
if D >= 0:
    x1 = round((-b + math.sqrt(D)) / (2 * a), 2)
    x2 = round((-b - math.sqrt(D)) / (2 * a), 2)
    print(x1, x2)
else:
    print("Not")

# work
a = 2
b = 4
c = 10

D = b ** 2 - (4 * a * c)
if D >= 0:
    x1 = round((-b + math.sqrt(D)) / (2 * a), 2)
    x2 = round((-b - math.sqrt(D)) / (2 * a), 2)
    print(x1, x2)
else:
    x1 = -b / (2 * a)
    x2 = math.sqrt(math.fabs(D)) / (2 * a)
    print(complex(x1, x2), complex(x1, -x2))
print()

# TODO Homeworks
# homework_1
password = 'gw2545H'
pass_split = set(password)
a = len(password) >= 5
c = len({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} & pass_split) > 0
d = len({'@', '#', '%', '&'} & pass_split) > 0
if a & c & d:
    print("Пароль безопасным")
else:
    print("Пароль не безопасным")
print()

# homework_4
price_list = {'smart watch': 600, 'phone': 1000, 'playstation': 450, 'laptop': 1550, 'music player': 400, 'tablet': 400}
shopping_basket_sum = price_list['smart watch'] + price_list['playstation'] + price_list['music player']
money = 1100
if shopping_basket_sum > 1000:
    new_sum = shopping_basket_sum - ((shopping_basket_sum * 30)/100)
    if (money - new_sum) >= 0:
        print('Можно купить')
    else:
        print("Не хватает денег")
else:
    if money > shopping_basket_sum:
        print('Можно купить')
    else:
        print('Не хватает денег')