a=[-1, 2, 0, 3, -4, 5]
d=int(input())
el=[x*d for x in a ]
count = sum(1 for x in a if x==d)
print(el)
print(count)
