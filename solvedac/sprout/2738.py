# 행렬이 뭘까..

# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
a = []
b = []
for i in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    b.append(list(map(int, input().split())))

res = []

for i in range(N):
    for j in range(M):
        res.append(a[i][j] + b[i][j])

cnt = 1
for x in res:
    if cnt % M == 0:
        print(x)
    else:
        print(x, end=" ")
    cnt += 1
