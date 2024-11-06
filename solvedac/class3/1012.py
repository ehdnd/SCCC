import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(u, v):
    q = deque()
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    q.append([u, v])
    V[u][v] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                nx < 0
                or nx > N - 1
                or ny < 0
                or ny > M - 1
                or not G[nx][ny]
                or V[nx][ny]
            ):
                continue
            q.append([nx, ny])
            V[nx][ny] = 1
    return


T = int(input())
while T:
    M, N, K = map(int, input().split())
    G = [[0 for _ in range(51)] for _ in range(51)]
    V = [[0] * 51 for _ in range(51)]
    for _ in range(K):
        u, v = map(int, input().split())
        G[v][u] = 1
    res = 0

    for n in range(N):
        for m in range(M):
            if G[n][m] and not V[n][m]:
                bfs(n, m)
                res += 1
    print(res)
    T -= 1
