N = int(input())
start = ord("z")
print("".join(chr(start - i) for i in range(N)))
