import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(graph):
    visit = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    for x, y in S:
        q.append([x, y])
        visit[x][y] = 1

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
                or graph[nx][ny]
            ):
                continue
            q.append([nx, ny])
            visit[nx][ny] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and visit[i][j] == 0:
                cnt += 1
    return cnt


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
S = []
W = []
for i in range(N):
    for j in range(M):
        if G[i][j] == 2:
            S.append([i, j])
        elif G[i][j] == 0:
            W.append([i, j])

res = 0
for i in range(len(W)):
    for j in range(i + 1, len(W)):
        for k in range(j + 1, len(W)):
            ax, ay = W[i]
            bx, by = W[j]
            cx, cy = W[k]
            G[ax][ay], G[bx][by], G[cx][cy] = 1, 1, 1
            res = max(res, bfs(G))
            G[ax][ay], G[bx][by], G[cx][cy] = 0, 0, 0
print(res)
