def is_square(k):
    return int(k**0.5)**2 == k
numbers = [4, 7, 9, 15, 16, 23, 25, 36, 50,81]
count = 0
for k in numbers:
    if is_square(k):
        count += 1
print(count)
