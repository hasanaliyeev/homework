text = "My name is Gasan Aliev. I am 30. I live in Volgodonsk"
all_symbol = len(text)

a = set(text)
print(len(a))

l1 = [5, 7, 1, 11, 6, 2, 3, 9, 4, 12]
l2 = [7, 1, 13, 4, 8, 9, 2, 14, 17, 34, 11, 6, 15, 27, 5]

s1 = set(l1)
s2 = set(l2)

m1 = s1.intersection(s2)
m2 = s1.symmetric_difference(s2)

t1 = s1 & s2
t2 = s1 ^ s2

print(m1, m2)
print(t1, t2)

a = sorted(m1)
print(a)
b = sorted(m2)
print(b)
print()

s1 = {1, 2}
s2 = {3}
s3 = {4, 5}
s4 = {3, 2, 6}
s5 = {6}
s6 = {7, 8}
s7 = {9, 8}

s = s1 | s2 | s3 | s4 | s5 | s6 | s7
count_s = len(s)
min_s = min(s)
max_s = max(s)
print('count:', count_s)
print('min:', min_s)
print('max:', max_s)
print()

drawing = {'Marina', 'Zhenya', 'Sveta'}
music = {'Kostya', 'Zhenya', 'Ilya'}

only_one_hobby = drawing.symmetric_difference(music)
print('Only one hobby:', only_one_hobby)
two_hobby = drawing.intersection(music)
drawing.symmetric_difference_update(two_hobby)
print(drawing)
music.symmetric_difference_update(two_hobby)
print(music)