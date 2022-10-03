greeting = 'hello world'
chars = []
for i in greeting:
    chars.append(i)
print(chars)

chars = [l for l in greeting]
print(chars)

chars = [c for c in 'my name is jon']
print(chars)

numbers = [i for i in range(1, 10)]
print(numbers)

numbers = [n**2 for n in range(1, 10)]
print(numbers)

numbers = [n for n in range(1, 10) if n % 2 == 0]
len_in_centimeters = [2, 21, 567, 267, 67]
len_in_meters = [round(n / 100, 2) for n in len_in_centimeters]
print(len_in_meters)

list1 = [2, 4, -5, 6, 8, -2]
list2 = [2, -6, 8, 3, 5, -2]

pairs = []
for l1 in list1:
    for l2 in list2:
        if l1 + l2 == 0:
            pairs.append((l1, l2))
print(pairs)

