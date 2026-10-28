def digit_count(k):
    return len(str(k))
numbers = [423,576346,76,234536453]
for k in numbers:
    print(k,digit_count(k))
