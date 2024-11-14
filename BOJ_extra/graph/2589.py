import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs():
    q = deque()
    q.append([n, m])
    V[n][m] = 1

    while q:
        x, y = q.popleft()
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                nx < 0
                or nx > N - 1
                or ny < 0
                or ny > M - 1
                or V[nx][ny]
                or G[nx][ny] == "W"
            ):
                continue
            q.append([nx, ny])
            V[nx][ny] = V[x][y] + 1
    return


N, M = map(int, input().split())
G = [list(input()) for _ in range(N)]
res = 0
for n in range(N):
    for m in range(M):
        if G[n][m] == "L":
            V = [[0] * M for _ in range(N)]
            bfs()
            res = max(res, max(map(max, V)))

print(res - 1)
