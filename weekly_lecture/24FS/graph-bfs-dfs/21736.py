import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(u, v):
    q = deque()
    q.append([u, v])
    V[u][v] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    res = 0
    while q:
        x, y = q.popleft()
        if G[x][y] == "P":
            res += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                nx < 0
                or nx > N - 1
                or ny < 0
                or ny > M - 1
                or V[nx][ny]
                or G[nx][ny] == "X"
            ):
                continue
            q.append([nx, ny])
            V[nx][ny] = 1

    return res if res != 0 else "TT"


N, M = map(int, input().split())
G = [list(input()) for _ in range(N)]
V = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if G[i][j] == "I":
            print(bfs(i, j))
