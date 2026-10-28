def quarter(x, y):
    if x > 0 and y > 0: return 1
    if x < 0 and y > 0: return 2
    if x < 0 and y < 0: return 3
    if x > 0 and y < 0: return 4

print(quarter(2, 5))
print(quarter(-3, 4))
print(quarter(1, -6))
