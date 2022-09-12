# List Methods

my_list = [1, 2, 3, 4, 5, 6, 7]
list.append(my_list, 9)
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 9]

new_list = [10, 11]
list.extend(my_list, new_list)
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]

list.insert(my_list, 1, 0)
print(my_list)  # [1, 0, 2, 3, 4, 5, 6, 7, 9, 10, 11]

list.remove(my_list, 4)
print(my_list)  # [1, 0, 2, 3, 5, 6, 7, 9, 10, 11]

list.pop(my_list, 1)
print(my_list)  # [1, 2, 3, 5, 6, 7, 9, 10, 11]

nums = [7, 6, 2, 5, 7, 6, 3, 7]
x = list.count(nums, 7)
print(x)  # 3

print(list.index(nums, 7))  # 0

y = list.sort(nums)
print(nums)  # [2, 3, 5, 6, 6, 7, 7, 7]

a = [1, 6, 3]
a.reverse()
print(a)
del a[1]
print(a)
a.remove(1)
print(a)
b = [2, 4, 1, 8]
a.extend(b)
print(a)
a.pop(0)
print(a)


