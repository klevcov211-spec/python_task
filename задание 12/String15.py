s = input()
count = 0
for ch in s:
    is_latin = "A" <= ch <= "Z" or "a" <= ch <= "z"
    is_cyrillic = "А" <= ch <= "Я" or "а" <= ch <= "я" or ch in "Ёё"
    if is_latin or is_cyrillic:
        count += 1
print(count)
