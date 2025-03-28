import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
G = [[0] * (101) for _ in range(101)]
for i in range(1, N + 1):
    G[i] = [0] + list(map(int, input()))
visit = [[0] * (M + 1) for _ in range(N + 1)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

q = deque()
q.append((1, 1))
visit[1][1] = 1

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 1 or nx > N or ny < 1 or ny > M or G[nx][ny] == 0 or visit[nx][ny]:
            continue
        visit[nx][ny] = visit[x][y] + 1
        q.append((nx, ny))

print(visit[N][M])

# for n in range(N):
#     for m in range(M):
#         print(visit[n + 1][m + 1], end=" ")
#     print()
