def roots_count(a, b, c):
    D=b**2-4*a*c
    if D>0:
        return 2
    elif D==0:
        return 1
    else:
        return 0
total_roots = roots_count(1, -3, 2) + roots_count(1, -2, 1) + roots_count(1, 1, 1)
print(total_roots)
