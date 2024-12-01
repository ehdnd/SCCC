import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inf = int(1e9)


def bfs(v):
    q = deque([v])
    V = [0] * (2 * N)
    while q:
        x = q.popleft()
        for nx, _ in G[x]:
            if not V[nx]:
                V[nx] = 1
                q.append(nx)
    return V[N + ed]


N, st, ed, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
C = list(map(int, input().split()))

G = [[] for _ in range(2 * N)]

# sol2) 정점 분할
for i in range(N):
    i_in = i
    i_out = N + i
    G[i_in].append([i_out, -C[i]])

for a, b, cst in lines:
    a_out = N + a
    b_in = b
    G[a_out].append([b_in, cst])

# 목적지 도달 가능 확인
P = [0] * (2 * N)
for x in range(2 * N):
    P[x] = bfs(x)

dist = [inf] * (2 * N)
dist[st] = 0

isCycle = False
for i in range(2 * N):
    for x in range(2 * N):
        if dist[x] == inf:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                if i == 2 * N - 1 and P[nx]:
                    isCycle = True


if dist[N + ed] == inf:
    print("gg")
elif isCycle:
    print("Gee")
else:
    print(-dist[N + ed])
