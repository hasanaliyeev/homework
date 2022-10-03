def min_num(a, b):
    if a < b:
        return a
    else:
        return b


def max_num(a, b):
    if a > b:
        return a
    else:
        return b


def max_num_list(x):
    s = 0
    for i in x:
        s += i
    return s


print(min_num(3, 8))
print(max_num(3, 8))
print(max_num_list([-2, 3, 9]))
print()


def fib(N):
    a, b = 0, 1
    while a < N:
        print(a, end=' ')
        a, b = b, a + b


fib(15000)
print()

ls = [3, 13, 27, 9, 4, 5, 16, 91, 77, 2]


def is_prime(x):
    no_simple = []
    simple = []
    for i in x:
        s = 0
        for k in range(1, i + 1):
            if i % k == 0:
                s += 1
        if s > 2:
            no_simple.append(i)
        else:
            simple.append(i)
    print('No Simple:', no_simple)
    print('Simple:', simple)
    print(min(simple))
    print(max(no_simple))


is_prime(ls)





