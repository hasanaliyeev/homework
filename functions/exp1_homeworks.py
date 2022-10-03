# Homework_1
ls = [2, 3, 5, 7, 15, 9, 24]


def find(n):
    for i in n:
        s = []
        for k in range(1, i + 1):
            if i % k == 0:
                s.append(k)
        print(i, s)


find(ls)

# Homework_2
ls = []