# work_1
def digits_sum(n, even=True):
    s = 0
    new_n = str(n)
    ls = []
    for i in new_n:
        ls.append(int(i))
    for i in ls:
        if i % 2 == 0 and even:
            s += i
        if i % 2 != 0 and not even:
            s += i
    return s


print(digits_sum(1256794))
print(digits_sum(567201, False))


# work_2
def find_num(num, *args):
    max_num = -1
    for i in args:
        if i > 0 and i % num == 0:
            max_num = i
    if max_num != -1:
        return max_num
    else:
        return 'No such numbers'


print(find_num(3, 3, 8, 3, 7, -13, 26, -39, 0, 2, 44, 77, 81))

# work_3
def square(figure_type, **kwargs):
    s = 0
    if figure_type == 'square':
        return kwargs['a'] * 4
    elif figure_type == 'rhombus':
        return kwargs['d1'] * kwargs['d2'] / 2

print(square('square', a=5))
print(square('rhombus', d1 = 10, d2=8))


