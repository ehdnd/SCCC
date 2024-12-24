import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(i, j, h):
    q = deque()
    q.append([i, j])
    V[i][j] = 1

    while q:
        x, y = q.popleft()
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                nx < 0
                or nx > N - 1
                or ny < 0
                or ny > N - 1
                or V[nx][ny]
                or G[nx][ny] <= h
            ):
                continue
            q.append([nx, ny])
            V[nx][ny] = 1
    return


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
m = max(map(max, G))

res = 0
for h in range(m + 1):
    temp = 0
    V = [[0] * N for _ in range(N)]
    S = []
    for i in range(N):
        for j in range(N):
            if not V[i][j] and G[i][j] > h:
                bfs(i, j, h)
                temp += 1
    res = max(temp, res)

print(res)
