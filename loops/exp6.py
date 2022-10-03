for i in 'hello world':
    if i == 'a':
        break
else:
    print('Not word "a"')

ingr = {'масло', 'мука', 'сахар', 'яйца', 'сливки', 'орехи', 'вишня', 'ванилин'}
masha_ingr = {'сахар', 'яблоки', 'груши', 'орехи', 'мед', 'маргарин', 'яйца', 'мука'}

for i in ingr:
    if i not in masha_ingr:
        print('Не хватает ингридиенти')
        break
else:
    print('Можно готовить')

ls = ['snow', 'rain', 'wind', 'sun', 'clouds']
for i in ls:
    if len(i) < 4:
        print('YES')
        break
else:
    print('NO')

ls = ['snow', 'rain', 'wind', 'sun', 'clouds']
k = 0
for i in ls:
    if len(i) < 4:
        k += 1
    if k == 2:
        print('YES')
        break
else:
    print('NO')

txt = 'My name is Gasan. I was born 10 june 1992. I live in Volgodonsk.'
txt = "GasanAliev12"
let_count = 0
num_count = 0
for i in txt:
    if i.isdecimal():
        num_count += 1
    elif i.isalpha():
        let_count += 1
    else:
        print(i, 'error')
        break
else:
    print(let_count, num_count)

# TODO Homeworks
# homework_1
ls = [1, 1, 3, 5, 7, 8]
for i in ls:
    if i % 2 == 0:
        print('Четное число:', i)
        break
else:
    print('Четные числа не найдены!')

# homework_2_1
txt = 'Python else loop'
b = False
for i in range(0, len(txt) - 1):
    if txt[i] == 'l':
        if txt[i + 1] in ['a', 'o', 'e']:
            print(txt[i + 1])
            b = True
if b == False:
    print('Искомые комбинации не найдены!')
print()

