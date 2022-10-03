l = [3, 4, 5, 6, 7, 9, 15, 16, 27, 21, 23, 25, 27, 100]


def func(n):
    for i in range(2, n):
        if n % i == 0:
            return True

res = filter(func, l)