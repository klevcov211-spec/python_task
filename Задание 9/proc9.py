def add_right_digit(d, k):
    return int(str(d) + str(k))
k=int(input())
d1=int(input("0-9 "))
d2=int(input("0-9 "))

k=add_right_digit(d1, k)
print(k)

k=add_right_digit(d2,k)
print(k)