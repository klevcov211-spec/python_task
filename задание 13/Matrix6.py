M=int(input())
N=int(input())
Q=int(input())
first_row = [int(input()) for _ in range(N)]
matrix = []
for i in range(M):
    row = [x * (Q ** i) for x in first_row]
    matrix.append(row)
for row in matrix:
    print(*row)
