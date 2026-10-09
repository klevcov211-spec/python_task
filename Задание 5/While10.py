N = int(input())
K = 0
while 3**(K + 1) < N:
    K += 1
print(K)
