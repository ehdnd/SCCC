import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(v):
    q = deque()
    q.append(v)
    visit[v[0]][v[1]] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 1 or nx > N or ny < 1 or ny > N or G[nx][ny] == 0 or visit[nx][ny]:
                continue
            q.append((nx, ny))
            visit[nx][ny] = 1
            cnt += 1
    return cnt


N = int(input())
G = [[0] * (26) for _ in range(26)]
for i in range(N):
    G[i + 1] = [0] + list(map(int, input()))
visit = [[0] * 26 for _ in range(26)]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

res = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if visit[i][j] == 0 and G[i][j] == 1:
            v = (i, j)
            res.append(BFS(v))

# for i in range(N):
#     for j in range(N):
#         print(visit[i + 1][j + 1], end=" ")
#     print()

res.sort()
print(len(res))
print(*res, sep="\n")
