a = [3, 7, 1, -2, 8, -4, 6, 9, 0, 5]
max_a = max(a)
index_max_a = a.index(max_a)
del a[index_max_a + 1:]
print(a)

b = [3, -7, 1, -2, 8, -4, 6, 9, 0, 5]
max_b = max(b)
min_b = min(b)
max_index = b.index(max_b)
min_index = b.index(min_b)
print(b)
del b[min_index+1:max_index]
print(b)

c = [3, -7, 1, -2, 8, -4, 6, 9, 0, 5]
c.sort(reverse=True)
print(c)

