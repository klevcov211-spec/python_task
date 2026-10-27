n={"hello":1,
   "dog":2,
   "cat":3,
}
m={"hi":1,
   "home":2,
   "horse":3,}
ign=0
for i,j in m.items():
    if i in n:
        ign=ign+1
    else:
        n[i]=j
print(len(n))
print(ign)
print(n)