A = [1, 2, 3, 4, 5, 6]
ind= A[::2]
total_sum = sum(ind)
total_prod = 1
for x in ind:
    total_prod *= x
print(total_sum)
print(total_prod)
