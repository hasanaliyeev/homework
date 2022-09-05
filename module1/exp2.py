a = [1, 2, 5]
b = []
c = [3, 7, 'pen', 4.7]
d = [2, 3, [4, 6]]
e = list('hello')  # ['h', 'e', 'l', 'l', 'o']
f = [f * 2 for f in 'list']  # ['ll', 'ii', 'ss', 'tt']

my_list = [True, 56, 78, 3.14, "text", [1, 'pen']]
x = my_list[1:4]  # [56, 78, 3.14]
y = my_list[1:]  # [56, 78, 3.14, 'text', [1, 'pen']]
z = my_list[:]  # [True, 56, 78, 3.14, 'text', [1, 'pen']]
g = my_list[:3]  # [True, 56, 78]
t = my_list[-1]  # [1, 'pen']
v = my_list[-3:-1]  # [3.14, 'text']

my_new_list = [1, 'car', 7, 3.45]
del my_new_list[1]
nums = [2, 4, 7, 9, 1, 8, 3, 5]
print(nums)
del nums[1:3]
print(nums)



