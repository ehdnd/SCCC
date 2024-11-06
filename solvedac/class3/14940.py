import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(u, v):
    q = deque()
    q.append([u, v])
    V[u][v] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                nx < 0
                or nx > N - 1
                or ny < 0
                or ny > M - 1
                or V[nx][ny]
                or not G[nx][ny]
            ):
                continue
            q.append([nx, ny])
            V[nx][ny] = V[x][y] + 1
    return


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
V = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if G[i][j] == 2:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if V[i][j] == 0 and G[i][j] == 0:
            print(0, end=" ")
        elif V[i][j] == 0 and G[i][j] == 1:
            print(-1, end=" ")
        else:
            print(V[i][j] - 1, end=" ")
    print()
