s_1 = set([1, 3, 5])
s_2 = set([2, 4, 6])
print(s_1.isdisjoint(s_2))  # True

a_1 = set([1, 2, 3])
a_2 = set([2, 3])
print(a_2.issubset(a_1))  # True

b_1 = set([1, 2, 3])
b_2 = set([1, 2, 3])
print(b_1.issuperset(b_2))  # True

A = set([1, 2, 3, 4, 5, 6])
B = set([1, 3, 5, 7])
print(A.union(B))  # {1, 2, 3, 4, 5, 6, 7}

A = set([1, 2, 3, 4, 5, 6])
B = set([1, 3, 5, 7])
print(A.intersection(B))  # {1, 3, 5}

A = set([1, 2, 3, 4, 5, 6])
B = set([1, 3, 5, 7])
print(A.difference(B))  # {2, 4, 6}
print(B.difference(A))  # {7}

A = set([1, 2, 3, 4, 7, 9])
B = set([2, 3, 5, 8, 9])
print(A.symmetric_difference(B))  # {1, 4, 5, 7, 8}

a = set()
a.add(1)
a.add(5)
a.add(3)
a.add(2)
a.add(4)
print(a)

a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 7, 8}
a.update(b)  # {1, 2, 3, 4, 5, 7, 8}

a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 7, 8}
a.difference_update(b)  # {1, 3}

a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 7, 8}
a.intersection_update(b)  # {2, 4, 5}

a = {1, 2, 3, 4, 5}
b = {2, 4, 5, 7, 8}
a.symmetric_difference_update(b)  # {1, 3, 7, 8}

a = {1, 3, 5, 7}
a.pop()  # {3, 5, 7}

a = {1, 3, 5, 7}
a.remove(3)  # {1, 5, 7}

a = {1, 3, 5, 7}
a.discard(7)  # {1, 3, 5}
