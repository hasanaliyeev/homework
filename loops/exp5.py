for i in range(0, 10):
    if i > 5:
        break
    print(i)
print()

i = 0
while i < 10:
    if i > 4:
        break
    print(i)
    i += 1
print()

for i in range(0, 5):
    if i == 3:
        continue
    print(i)
print()

i = 0
while i < 7:
    i += 1
    if i == 3:
        continue
    print(i)
print()

products = {'milk': '', 'bread': 'v', 'pie': '', 'cherry': 'v', 'cucumbers': 'v', 'cheese': '', 'cream': '',
            'chocolate': 'v'}
for k, v in products.items():
    if v == 'v':
        continue
    print(k)
print()

words = 'Break and Continue operators'
k = 0
for i in range(0, len(words)):
    if words[i] == 'p':
        print(words[i], end='')
        break
    if i > 0 and (i + 1) % 3 == 0:
        continue
    print(words[i], end='')

print()
print()

words = ['snow', 'rain', 'wind', 'sun', 'clouds']
for i in words:
    if len(i) <= 3:
        continue
    print(i, end=' ')
print()

for i in words:
    if len(i) == 3:
        break
    print(i, end=' ')
print()
print()

name = input('name: ')
psw = input('password: ')
while True:
    if len(psw) < 8:
        print('Too short password')
    elif name in psw:
        print('Password contains name')
    else:
        print('Password was set')
        break
    psw = input('password: ')
print()
