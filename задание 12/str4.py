n=int(input())
start = ord("A")
print("".join(chr(start + i) for i in range(n)))
