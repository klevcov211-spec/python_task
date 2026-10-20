def invert_digits(k):
    r=0
    while k > 0:
        r=r*10+k%10
        k //= 10
    return r
for i in range(5):
    num=int(input(i+1))
    print(invert_digits(num ))
