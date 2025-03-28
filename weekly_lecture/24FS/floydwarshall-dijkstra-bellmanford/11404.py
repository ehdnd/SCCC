import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = int(input()), int(input())
dist = [[1e9] * (101) for _ in range(101)]
for i in range(N + 1):
    dist[i][i] = 0

for _ in range(M):
    st, ed, cst = map(int, input().split())
    dist[st][ed] = min(dist[st][ed], cst)

for x in range(1, N + 1):
    for st in range(1, N + 1):
        for ed in range(1, N + 1):
            dist[st][ed] = min(dist[st][ed], dist[st][x] + dist[x][ed])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(dist[i][j], end=" ") if dist[i][j] < 1e9 else print(0, end=" ")
    print()
