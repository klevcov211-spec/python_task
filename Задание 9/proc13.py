def sort_dec3(a, b, c):
    if a<b:
        a,b=b,a
    if b<c:
        b,c=c,b
    if a<b:
        a,b=b,a
    return a,b,c
a1,b1,c1=10,25,15
a1,b1,c1=sort_dec3(a1,b1,c1)
print(a1,b1,c1)
a2,b2,c2=4,-2,8
a2,b2,c2=sort_dec3(a2,b2,c2)
print(a2,b2,c2)

