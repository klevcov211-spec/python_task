import math
def triangle_ps(a):
    return 3*a, a**2 * math.sqrt(3)
a=float(input())
print(triangle_ps(a))