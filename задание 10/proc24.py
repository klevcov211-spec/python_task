def even(k):
    return k % 2 == 0
numbers = [12, 5, 8, 3, 14, 21, 6, 9, 10, 7]
count = 0
for k in numbers:
    if even(k):
        count += 1
print(count)
