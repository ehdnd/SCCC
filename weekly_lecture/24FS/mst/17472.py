import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(u, v, node):
    q = deque()
    q.append([u, v])
    V[u][v] = node

    while q:
        x, y = q.popleft()
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
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
            V[nx][ny] = node

    return


def Find(a):
    if S[a] < 0:
        return a
    S[a] = Find(S[a])
    return S[a]


def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a == b:
        return False
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return True


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
V = [[0] * 10 for _ in range(10)]
Lines = []
S = [-1] * 7

# 섬 번호 매기기
node = 0
for n in range(N):
    for m in range(M):
        if G[n][m] and not V[n][m]:
            node += 1
            bfs(n, m, node)

# 간선 만들기
for n in range(N):
    for m in range(M):
        if V[n][m]:
            a = V[n][m]
            nx, ny = n, m
            dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
            for i in range(4):
                cnt = 0
                b = 0
                while 1:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1 or V[nx][ny] == a:
                        break
                    if V[nx][ny] and V[nx][ny] != a:
                        b = V[nx][ny]
                        break
                    cnt += 1
                if cnt > 1 and b != 0:
                    Lines.append([cnt, a, b])

Lines.sort()

res = 0
isCon = False
for w, u, v in Lines:
    if Union(u, v):
        res += w
    if -S[Find(u)] == node:
        isCon = True
        break

print(res) if res != 0 and isCon else print(-1)
