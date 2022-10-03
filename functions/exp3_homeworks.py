# homework_1
my_tuple = ('home', 'body', 'apple', 'book', 'car', 'length', 'milk', 'money')
sorted_tuple = sorted(my_tuple, key=lambda n: n[-2])
print(sorted_tuple)

# homework_2_1
emp = [{'name': 'Gasan', 'city': 'Volgodonsk', 'age': 30}, {'name': 'Farid', 'city': 'Baku', 'age': 27},
       {'name': 'Alsu', 'city': 'Volgodonsk', 'age': 3}, {'name': 'Jon', 'city': 'London', 'age': 35},
       {'name': 'Aleks', 'city': 'Toronto', 'age': 18}]

sorted_emp = sorted(emp, key=lambda n: n.get('age'))
print(sorted_emp)


# homework_2_2
def sorted_func(n):
    return sorted(n, key=lambda x: x.get('name'))


print(sorted_func(emp))

# homework_3_1
my_list = [4, 5, 7, 11, 24, 35, 47, 81]


def func(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return True
    else:
        return False


res = filter(func, my_list)
print(list(res))

# homework_4_1
l1 = [1, 2, 3]
l2 = [4, 5, 6]
lmd = map(lambda x, y: x + y, l1, l2)
print(list(lmd))

# homework_3_2
ls = [4, 5, 7, 11, 24, 35, 47, 81]
def count(n):
    return lambda x: list(range(2, x))

res = count(ls)
print(res(12))