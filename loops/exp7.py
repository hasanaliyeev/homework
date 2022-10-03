m = [[1, 2, -3, 4],
     [3, 2, 1, 19],
     [-9, 1, 7, 24]]
for i in range(0, len(m)):
    for k in range(0, len(m[i])):
        print(m[i][k], end='\t')
print()
x = 0
x_max = 0
for i in range(0, len(m)):
    for k in range(0, len(m[i])):
        x = m[i][k]
        if x > x_max:
            x_max = x
print(x_max)

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
a = []
m_sum = 0
for i in range(0, len(m)):
    for k in range(0, len(m[i])):
        m_sum += m[i][k]

print(m_sum)
