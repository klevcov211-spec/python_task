a=[14,3464,5456,335,3324,]
s=sum(a)/len(a)
el=[x for x in a if x>=s]
print(el)
print(s)