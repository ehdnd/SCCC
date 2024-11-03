import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(G, N, M):
    q = deque()
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1:
                q.append([i, j])
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
                or G[nx][ny] >= 1
                or G[nx][ny] == -1
            ):
                continue
            q.append([nx, ny])
            G[nx][ny] = G[x][y] + 1

    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                return -1

    return max(map(max, G)) - 1


M, N = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

print(BFS(G, N, M))
