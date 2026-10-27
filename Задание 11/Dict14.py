n={"hello":1,
   "dog":2,
   "cat":3,
}
v=int(input())
d={}
for i,j in n.items():
    if j>=v:
        d[i]=j
print(d)