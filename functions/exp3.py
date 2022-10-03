# Пример 1
func = lambda x, y: x + y
print(func(3, 7))
print(func('a', 'b'))
print((lambda x, y, z: x + y + z)(1, 3, 7))
print((lambda a, b, c: 2 * a + 3 * b + 4 * c)('x', 'y', 'z'))

# Пример 2
func = lambda *args: args
print(func(1, 2, 3, 5, 5))
print(func('a', 'b', 'c'))
print((lambda *args: args)('gasan', 'farid', 'alsu', 'gyunel'))


# Пример 3
def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(10)
print(f(12))

# Пример 4
pairs = [(2, 'two', 61), (1, 'one', 7), (4, 'four', 8), (3, 'three', 9)]
pairs.sort(key=lambda pair: pair[0])
print(type(pairs), pairs)
pairs.sort(key=lambda pair: pair[2])
print(type(pairs), pairs)

# Пример 5
ls = ['a', 'aaa', 'aaaa', 'bb', 'c']
print(sorted(ls, key=len))
print(sorted(ls, key=len, reverse=True))
print(sorted(ls))


# Пример 6
def func(x):
    return x % 7


ls = [15, 3, 11, 7]
print(sorted(ls, key=func))


# Пример 6
def func1(variable):
    vovels = ['a', 'e', 'o', 'i']
    return variable in vovels


seq = ['g', 'w', 'e', 'a', 'gasan']
res = filter(func1, seq)
print(list(res))

# Пример 7
res = filter(lambda x: x in ['a', 'b', 'c'], seq)
print(list(res))

# Пример 8
seq = ['a', 'o', 'i', 'e', 'u']
res = filter(lambda x: x in ['a', 'i'], seq)
print(list(res))


# Пример 9
def func2(variable):
    vovels = ['a', 'b', 'c']
    return variable in vovels


seq = ['a', 'c', 'e', 'd']
test = filter(func2, seq)
print(list(test))

# Пример 10
scores = [12, 56, 76, 7, 42, 9, 1, 89, 17, 7, 98, 112]


def func3(x):
    return x > 10


test = filter(func3, scores)
print(list(test))

# Пример 11
scores = [12, 56, 76, 7, 42, 9, 1, 89, 17, 7, 98, 112]
t = list(filter(lambda x: x > 10, scores))
print(t)

# Пример 12
ls = ['pen', 'book', 'car', 'money', 'life']
res = list(map(list, ls))
print(res)

# Пример 13
nums = [3.12345, 5.12345, 6.12345, 8.12345, 2.12345]
res = list(map(round, nums, range(1, 5)))
print('results:', res)


# Пример 14
def addition(n):
    return n + n


nums = [1, 3, 7, 9]
res = list(map(addition, nums))
print(res)


# Пример 15
def rnd(n):
    return round(n, 2)


nums = [1.2362, 6.25662, 8.212]
res = list(map(rnd, nums))
print(res)

# Пример 16
def flt(n):
    if ('a' or 'e') in n:
        return n

ls = ['gasan', 'farid', 'alsu', 'gyunel', 'rom']
res = list(map(flt, ls))
print(res)
print(list(filter(lambda x :len(x) > 4, ls)))

# Пример 17
def adn(n):
    return n + n

res = list(map(adn, [2, 3, 4]))
print(res)

# Пример 18
res = list(map((lambda x : x + x), [1, 2, 3]))
print(res)





