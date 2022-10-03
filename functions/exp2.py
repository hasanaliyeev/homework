def func1():
    print('Function without arguments')


func1()


def func2(arg='None'):
    print(arg)


func2()

i = 5


def func3(arg=i):
    print(arg)


i = 6

func3()


def func4(a, L=[]):
    L.append(a)
    return L


func4(3)
print(func4(7))
print(func4(2))


def func5(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(func5(2))
print(func5(9))
print(func5(8, [0, 1]))


def func6(*args):
    print(args)


func6(8, 78, [1, 2, 3], 'abs')


def func7(a, *args):
    print(a, args)


func7(2, 3, 4, ['a', 'b'])


def concat(*args, sep='/'):
    return sep.join(args)


print(concat('gasan', 'aliev', sep='-'))


def func8(**kwargs):
    return kwargs


print(func8(a=1, b=2, c=3))
print(func8(a='Gasan', b ='Alsu', c='Gyunel'))


def func9(*args):
    print(args[1])


func9('a', 'b', 'c')


def func10(**kwargs):
    print(kwargs['first'])


func10(first='1', second='2', third='3')



