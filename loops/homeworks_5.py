# homework_1_1
ls = list(range(1, 10))
s = 0
k = 0
for i in ls:
    if s != 15:
        s += i
        k += 1
    else:
        break
print(s, k)
print()

# homework_1_2
ls = list(range(1, 10))
k = 0
i = 0
s = 0
d = 15
while i < len(ls):
    n = ls[i]
    if s == d or s > d:
        break
    s += n
    k += 1
    i += 1
print(s, k)
print()

# homework_3
ls = ['Rose', 'Nina', 'Phillip', 'Alex', 'Jimmy', 'Max']
for i in ls:
    if len(i) <= 4:
        if 'x' in i:
            print(i.replace('x', ''))
        else:
            print(i)
print()

# homework_4
login = input('Login: ')

while True:
    psw = input('Password: ')
    if len(psw) < 8:
        print('Short password')
        continue
    elif psw in login:
        print('Password contains login')
        continue
    else:
        print('Password was set')
        break
