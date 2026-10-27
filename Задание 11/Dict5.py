n={"hello":1,
   "dog":2,
   "cat":3,
}
k=input()
if k in n:
    n.pop(k,0)
    print(n)
else:
    print(n)