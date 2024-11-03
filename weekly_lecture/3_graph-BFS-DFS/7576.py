import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(tomato, visit):
    q = deque(tomato)
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
                or visit[nx][ny]
                or G[nx][ny] == -1
            ):
                continue
            q.append([nx, ny])
            visit[nx][ny] = visit[x][y] + 1

    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0 and G[i][j] == 0:
                return -1

    return max(map(max, visit)) - 1


M, N = map(int, input().split())
G = [[-1] * 1010 for _ in range(1010)]
visit = [[0] * 1010 for _ in range(1010)]
for i in range(N):
    G[i] = list(map(int, input().split()))

tomato = []
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            tomato.append([i, j])
            visit[i][j] = 1

print(BFS(tomato, visit))

# for i in range(N):
#     for j in range(M):
#         print(visit[i][j], end=" ")
#     print()
