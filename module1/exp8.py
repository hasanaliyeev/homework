import math

a = bytes.fromhex("5e ")

b = b"abc"
b = b.replace(b"a", b"x")

b = b'1,2,3'.split(b',')

b = b'1,2,3,4'.split(b',', maxsplit=2)

b = b'abc'.decode()

b = bytearray(b'abc').decode()

text = b"My name is Gasan (Aliev. I live in) Volgodonsk"
first_index = text.index(b'(')
last_index = text.index(b')')
new_binary_text = text[first_index + 1:last_index]

s = "Some very-very long string"
bytes_s = s.encode()
bytearray_s = bytearray(bytes_s)
bytearray_s[2::3] =