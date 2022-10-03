def func(n):
    return lambda x: x * n


res = func(2)
print(res(15))
print(res(10))

ls = ['gasan', 'farid', 'alsu', 'gyunel', 'pen', 'book']
res = sorted(ls, key=lambda i: i[1])
print(res)

st = 'gasanaliev'

res = lambda s: True if s.startswith('g') else False
print(res(st))
res = lambda s: s.startswith('a')
print(res('yali'))

def start_with(n):
    return n.startswith('g')

print(start_with('gasan'))

def end_with(word, suffix):
    return word.endswith(suffix)

print(end_with('aliev', 'v'))

def st_with(letter):
    return lambda x: x.startswith(letter)

res = st_with('A')
print(res('PApple'))

words = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']
res = filter(lambda word: word == word[::-1], words)
print(list(res))

nums = [2, 3, 4, 5]

square = list(map(lambda x : x**2, nums))
cube = list(map(lambda x : x**3, nums))
print(square)
print(cube)


