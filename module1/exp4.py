# Tuple

a = (1, 3, 5, 7, 'pen', 9)
b = (2, 4, 6, 8)
c = a * 2  # (1, 3, 5, 7, 'pen', 9, 1, 3, 5, 7, 'pen', 9)
d = (1,)  # (1,)
my_tuple = (3, 'text', 7)
x, y, z = my_tuple
print(x)  # 3
print(y)  # text
print(z)  # 7

# List range

list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(1, 7))  # [1, 2, 3, 4, 5, 6]
list(range(2, 15, 3))  # [2, 5, 8, 11, 14]
list(range(10, 100, 20))  # [10, 30, 50, 70, 90]
list(range(0, -10, -2))  # [0, -2, -4, -6, -8]
list(range(0))  # []
list(range(1, 0))  # []
list(range(1, 0, -1))  # [1]

my_list = [2, 9, 'pen', 'car', 3, 7]
2 in my_list  # True
4 in my_list  # False
3 not in my_list  # False
6 not in my_list  # True

first_list = [1, 5, 7]
second_list = [2, 4, 6, 8]
my_new_list = first_list + second_list[0:2]  # [1, 5, 7, 2, 4]

nums = [1, 'pen', 2]
new_nums = nums * 3  # [1, 'pen', 2, 1, 'pen', 2, 1, 'pen', 2]
len(new_nums)  # 9

nums = [2, 5, 1, 8, 7, 17, 25, 9, 7]
min(nums)  # 1
max(nums)  # 25
sum(nums)  # 81

nums = [3, 1, 6, 7, 3, 67, 12, 2, 1]
print(sorted(nums))  # [1, 1, 2, 3, 3, 6, 7, 12, 67]
print(sorted(nums, reverse=True))  # [67, 12, 7, 6, 3, 3, 2, 1, 1]

nums = [1, 4, 6, 2, 3, 7, 2]
print(nums.index(2))  # 3
print(nums.index(2, 5))  # 6

nums = (list(range(10))) * 2
sum_l = sum(nums)  # 90
print(sum_l)

l = [2, -5, -1, 9, -3, 7, 4]
sort_l = sorted(l, reverse=True)  # [9, 7, 4, 2, -1, -3, -5]
print(sort_l)

my_list = [2, -1, -9, 3, 7, 8, -4, 6]
max_e = max(my_list)
my_list.remove(max_e)
my_list.insert(0, max_e)
print(my_list)

l = [2, -5, -7, -3, -8, 4, 9, -1, 5, 7]
l_min = min(l)
min_i = l.index(l_min)

del l[0:min_i]

