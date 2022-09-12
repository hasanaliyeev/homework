# String and methods

text = 'Hello, Python!'
new_text = text[:5]  # Hello
new_text = text[7:]  # Python!
new_text = text[-5:-1]  # thon
new_text = text[::3]  # Hl tn
new_text = text[::-1]  # !nohtyP ,olleH

b = 'l' in text  # True
b = 'o' not in text  # False
b = 'c' not in text  # True

str1 = 'Hello'
str2 = 'Gasan'
str3 = str1 + str2;
str4 = str1 * 3;
print(str1[-1] * 5)
print(len(str1))

name = 'Gasan Aliev'
min_name = min(name)
max_name = max(name)
lens_name = len(name)
print(name.count('l'))
print(name.index('n'))
print(name.index('a', 2))
print()

# Methods

text = "hello Gasan Aliev and Python"
text.capitalize()  # Hello gasan aliev and python

text = "Kolololo".count("olo")  # 2
text = "Kolololo".count("lo", 3)  # 2

text = "Gasan".startswith("Gas")  # True
text = "hello".endswith("lo")  # True

text = 'gasan\tsalam\tnecesen'.expandtabs(2)
print(text)

text = "my name is gasan aliev"
text_find = text.find("a")
text_find = text.rfind("a")
print(text_find)

text = "12345wwjj"
text.isalnum()  # True

text = "jasjhsa"
text.isalpha()  # True

text = "23542"
text.isdecimal()  # True

text = "shj"
text.islower()  # True

text = "FHFHJL"
text.isupper()  # True

text = "GasAliev"
text.lower()  # gasaliev

text.upper()  # GASALIEV

text = " ".join(["aaa", "bbb", "ccc"])  # aaa bbb ccc
text = ", ".join(["aaa", "bbb", "ccc"])  # aaa, bbb, ccc

text = "42".rjust(6)  #    42
text = "42".rjust(5,"_")  # ___42
text = "42".ljust(7, "-")  # 42-----
text = "42".zfill(8)  # 00000042

text = "   gasan   ".lstrip()  # "gasan   "
text = "www.example.com".lstrip("w.")  # "example.com"
text = "  gasan  ".rstrip()  # "  gasan"
text = "www.example.com".rstrip("com.")  # "www.example"
text = " gasan  ".strip()  # "gasan"
text = "www.example.com".strip("w.em")  # "xample.co"

text = "mynameisgasan".partition("name")  # ('my', 'name', 'isgasan')
text = "mynameisgasan".rpartition("my")  # ('', 'my', 'nameisgasan')
text = "hellobromynameisgasanaliev".partition("lds")  # ('hellobromynameisgasanaliev', '', '')
text = "hellobromynameisgasanaliev".partition("bro")  # ('hello', 'bro', 'mynameisgasanaliev')
text = "hellobromynameisgasanaliev".rpartition("is")  # ('hellobromyname', 'is', 'gasanaliev')

text = "Hello my best friends".replace("e","-")  # H-llo my b-st fri-nds
text = "Hello my best friends".replace("e","-",2)  # H-llo my b-st friends
text = "www.example.com".replace("w","")  # .example.com

text = "my name is gasan aliev".split(" ")  # ['my', 'name', 'is', 'gasan', 'aliev']
text = "1,2,3,4".split(",")  # ['1', '2', '3', '4']
text = "1,2,3,4".split(",",maxsplit=1)  # ['1', '2,3,4']
text = "my name is gasan".split()  # ['my', 'name', 'is', 'gasan']
text = "1 2 3 4 5".split()  # ['1', '2', '3', '4', '5']

text = "My Name is gAsan".swapcase()  # My Name is gAsan


