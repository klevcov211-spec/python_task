M=int(input())
N=int(input())
values = [int(input()) for _ in range(M)]
matrix = []
for i in range(M):
    row = [values[i]] * N
    matrix.append(row)
for row in matrix:
    print(*row)
