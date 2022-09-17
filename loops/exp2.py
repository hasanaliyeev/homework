# Loops 'while'
from math import pi, e, sin, cos

i = 1
print('START')
while i < 6:
    print(i)
    i += 1
print('END')
print()

# work_1
N = 0
while N <= pi:
    y = e ** sin(N) * cos(N)
    print(round(N, 3), round(y, 3))
    N += 0.1
print()

# work_2
A = 54
B = 81
while A != B:
    if A > B:
        A -= B
    else:
        B -= A
print('НОД:', A)
print()

# work_3
i = 2
summa = 0
N = 20
while i <= N:
    summa += i
    i += 2
print(summa)
print()

# work_4
my_list = [1452, 11.23, 1 + 2j, True, 'hello, python!', (0, -1), [5, 12], {'class': 'v', 'section': 'A'}]
size = len(my_list)
i = 0
while i < size:
    elem = my_list[i]
    print(elem, type(elem))
    i += 1
print()

# work_5
l = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
i = 0
while i < len(l):
    element = l[i]
    if ((element % 5) == 0) & (element <= 150):
        print(element)
    i += 1
print()

# TODO Homeworks
# homework_2
num_list = list(range(0, 7))
i = 0
while i < len(num_list):
    element = num_list[i]
    if element != 3 and element != 5:
        print(element)
    i += 1
print()

# homework_3
nums = list(range(100, 401))
i = 0
while i < len(nums):
    element = nums[i]
    print(element)
    i += 2
print()

# homework_4
n = 100
i = 1
summa = 0
while i <= n:
    summa += i
    i += 1
print('Factorial:', summa)
print()

# homework_5
x = '2'
i = 1
n = 7
summa = 0
while i <= n:
    value = int(x * i)
    summa += value
    i += 1
print('SUMMA:', summa)
