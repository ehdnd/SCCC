import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(C, u, v, G, V):
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
                or ny > N - 1
                or V[nx][ny]
                or G[nx][ny] != C
            ):
                continue
            q.append([nx, ny])
            V[nx][ny] = 1
    return


def jud(G):
    V = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not V[i][j]:
                bfs(G[i][j], i, j, G, V)
                cnt += 1
    return cnt


N = int(input())
A = [input() for _ in range(N)]
B = A.copy()
for i in range(N):
    B[i] = B[i].replace("G", "R")

print(jud(A), end=" ")
print(jud(B))
