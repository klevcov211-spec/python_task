M=int(input())
N=int(input())
D=int(input())
values=[int(input()) for _ in range(M)]
matrix=[]
for i in range(M):
    row=[values[i]+D*j for j in range(N)]
    matrix.append(row)
for row in matrix:
    print(*row)
