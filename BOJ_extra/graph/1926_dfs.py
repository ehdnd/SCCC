import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def dfs(x, y):
    V[x][y] = 1
    res = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1 or V[nx][ny] or not G[nx][ny]:
            continue
        res += dfs(nx, ny)

    return res


N, M = map(int, input().split())
G = [list(map(int, input().split())) for i in range(N)]
V = [[0] * 501 for _ in range(501)]

res = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if not V[i][j] and G[i][j]:
            res = max(res, dfs(i, j))
            cnt += 1

print(cnt)
print(res)
