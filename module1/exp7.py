text = "Ежевики для ежат " \
       "Принесли два ежа." \
       "Ежевики еле-еле " \
       "Ежата возле ели съели"
text_E = text.count("Е")
text_e = text.count(" е")
text_res = text_E + text_e;
print("Count:", text_res)

text = "My name is, Gasan Aliev."
text_without = text.replace(".", "")
text_without = text_without.replace(",", "")
text_split = text_without.split()
text_count = len(text_split)
print("Count words:", text_count)

text = "My name is Gasan (Aliev. I live in) Volgodonsk"
text_l = text.index("(")
text_r = text.index(")")
new_text = text[text_l + 1:text_r]
print(new_text)

text = "My name is Gasan Aliev. I live in Volgodonsk. " \
       "Volgodonsk big city. My daughther name is Alsu. " \
       "She 12. City big. I love my city"
our_word = "city"
low_al_word = text.lower()
word_count = low_al_word.count(our_word)
print("Count: ", word_count)

our_letter = "g"
count_1 = text.count(our_letter + " ")
count_2 = text.count(our_letter + ".")
count_3 = text.count(our_letter + ",")
all_count = count_1 + count_2 + count_3;
print("Count: ", all_count, "(" + our_letter + ")")

print("All letter count: ", low_al_word.count(our_letter))

text = "Import"
print(text.replace(""," ").strip())

