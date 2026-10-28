m=int(input())
n=int(input())
matrix = []
for i in range(m):
    row = [5 * j for j in range(1, n + 1)]
    matrix.append(row)
for row in matrix:
    print(*row)
