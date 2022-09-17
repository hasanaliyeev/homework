# Dictionary

my_dict = {}
my_dict["country"] = "Mexico"

new_dict = {"number": 7, 3: True, "my_list": [1, 2, 3, 2], "my_set": {1, 2, 2, 3, "pen"}, "my_tuple": (1, 2, 3)}
new_dict.keys()  # dict_keys(['number', 3, 'my_list', 'my_set', 'my_tuple'])
new_dict.values()  # dict_values([7, True, [1, 2, 3, 2], {1, 2, 3, 'pen'}, (1, 2, 3)])
new_dict["my_set"]  # {3, 1, 2, 'pen'}

school_info = {'name': 'Gasan Aliev', 'age': 30, 'profession': 'IT Manager', 'phones': ['123', '123312', '123213']}
school_info  # {'name': 'Gasan Aliev', 'age': 30, 'profession': 'IT Manager', 'phones': ['123', '123312', '123213']}

my_work = {'Gasan Aliev': {"name": "Gasan", "family": "Aliev", "age": 30, "profession": "IT Manager"},
           'Farid Aliev': {"name": "Farid", "family": "Aliev", "age": 27, "profession": "Python Developer"}}

a = {"one": 1, "two": 2, "three": 3}
b = dict(one=1, two=2, three=3)
c = dict([("one", 1), ("two", 2), ("three", 3)])
d = dict({"three": 3, "one": 1, "two": 2})
e = a == b == c == d  # True

len(a)  # 3

# методы
my_info = {}
my_info["name"] = "Gasan"
my_info["family"] = "Aliev"
my_info["age"] = 30
my_info["profession"] = "IT Manager"

my_info["city"] = "volgodonsk"

my_info["profession"] = "Python Developer"
del my_info["city"]

x = {1: "one", 2: "two", 3: "three"}
iter(x)  # <dict_keyiterator object at 0x000001A10D3F94E0>
list(iter(x))  # [1, 2, 3]
1 in x  # True
3 not in x  # False
x.clear()  # {}

x = {1: "Gasan Aliev", "my_list": [1, 2, 3, 4, 3], "my_tuple": (2, 3, 6)}
x.get("my_list")  # [1, 2, 3, 4, 3]
x.get("3")  # None
x.get("5", "Not Found")  # Not Found
y = x.copy()  # {1: 'Gasan Aliev', 'my_list': [1, 2, 3, 4, 3], 'my_tuple': (2, 3, 6)}

x.items()  # dict_items([(1, 'Gasan Aliev'), ('my_list', [1, 2, 3, 4, 3]), ('my_tuple', (2, 3, 6))])

x.pop(10, "Not Found key")  # Not Found key
x.popitem()
x.setdefault(2, "Farid")  # {1: 'Gasan Aliev', 'my_list': [1, 2, 3, 4, 3], 2: 'Farid'}
x.setdefault(1, "DEF")  # {1: 'Gasan Aliev', 'my_list': [1, 2, 3, 4, 3], 2: 'Farid'}
x.clear()
y.clear()

x = {1: "pen", 3: [2, 3], "name": "Gasan"}
y = {7: (2, 3, 3, 4), 1: "book", "name": "Alsu", "age": 30}
x.update(y)  # {1: 'book', 3: [2, 3], 'name': 'Alsu', 7: (2, 3, 3, 4), 'age': 30}

my_dict.clear()

my_dict = {1: "one", 2: "two", 3: "three"}
keys = my_dict.keys()  # dict_keys([1, 2, 3])
my_dict.update({4: "four"})
keys  # dict_keys([1, 2, 3, 4])
my_dict.pop(1)
keys  # dict_keys([2, 3, 4])

# works
a = {0: 10, 1: 20}
a[2] = 30
a.clear()

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {5: 50, 6: 60}
a.update(b)
a.update(c)

ds = {'data1': 100, 'data2': -54, 'data3': 247}
new_values = ds.values()
sum_values = sum(new_values)
d.clear()

d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
values = d.values()
v = sorted(values, reverse=True)
print('3 max elements: ', v[:3])
d.clear()

d_1 = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
d_2 = {'name': d_1.pop('name'), 'age': d_1.pop('age')}

info = {'name': 'Gasan', 'age': 30, 'city': 'New York'}
info['location'] = info.pop('city')
print(info)

employees = {'emp1': {'name': 'Gasan', 'salary': 7500},
             'emp2': {'name': 'Alsu', 'salary': 8000},
             'emp3': {'name': 'Gyunel', 'salary': 6500}}
employees['emp3']['salary'] = 8500
print(employees)
d.clear()

# TODO Homeworks
# work-1
d = {'v': 's001', 'v1': 's002', 'v2': 's001', 'v3': 's005', 'v4': 's005', 'v5': 's009', 'v6': 's007'}
values = d.values()
new_values = set(values)
print('Values:', new_values)

# work-2
d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}


