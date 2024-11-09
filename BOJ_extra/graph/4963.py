import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(i, j):
    q = deque()
    q.append([i, j])
    V[i][j] = 1

    while q:
        x, y = q.popleft()
        dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, -1, 1, 1, -1]
        for i in range(8):
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
            V[nx][ny] = 1
    return


while 1:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    res = 0
    G = [list(map(int, input().split())) for _ in range(N)]
    V = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if G[i][j] and not V[i][j]:
                bfs(i, j)
                res += 1
    print(res)
