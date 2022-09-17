for x in range(0, 6):
    print(x)
print()

for x in [1, 2, 3]:
    print(x)
print()

my_list = [2, 'pen', {'id': 1, 'name': 'gasan'}]
for i in my_list:
    print(i, len(my_list))
print()

words = ['cat', 'window', 'human']
for w in words:
    print(w, len(w))

words = ['pen', 'car', 'dog', 'pencil']
for w in words[:]:
    if len(w) > 3:
        words.insert(0, w)
print(words)
print()

for i in range(0, 5, 2):
    print(i)
print()

a = ['gasan', 'alsu', 'gyunel', 'farid']
for i in range(len(a)):
    print(i, a[i])
print()

# works
N = 8
f = 1
for i in range(1, (N + 1)):
    f *= i
print(f)
print()

n = 35
n_list = []
for i in range(1, n):
    if (n % i) == 0:
        n_list.append(i)
print(n_list, len(n_list))
print()

num_list = [11, 2, 33, 865, 56, -98, 43254, 445672, 67, 100, -33, -6]
max_num = num_list[0]
for i in range(1, len(num_list)):
    if num_list[i] > max_num:
        max_num = num_list[i]
print('Max:', max_num)
print()

# TODO Homeworks
# homework_1
N = 10
summa = 0
for i in range(0, N):
    summa += i
print('Summa:', summa)
print()

# homework_2
N = 91
k = 0
for i in range(2, N):
    if N % i == 0:
        k += 1
if k > 0:
    print(N, 'Не простой число')
else:
    print(N, 'Простой число')
print()

# homework_3
l = list(range(2, 15))
k = 0
s = 0
for i in l:
    for x in range(2, i):
        if i % x == 0:
            k += 1
    if k <= 0:
        s += 1
    k = 0
print('Simple nums:', s)

# homework_4
l = [3, 1, 66, 23, 7, 98, 56, 77, 7, 3, 17, -6, -234, -67, 67, 12, -1, -23, 99]
