import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inf = int(1e9)


def bfs(v):
    q = deque([v])
    V = [0] * N
    while q:
        x = q.popleft()
        for nx, _ in G[x]:
            if not V[nx]:
                V[nx] = 1
                q.append(nx)
    return V[ed]


N, st, ed, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, cst = map(int, input().split())
    G[a].append([b, cst])
C = list(map(int, input().split()))

# 목적지 도달 가능 확인
P = [0] * N
for x in range(N):
    P[x] = bfs(x)

# sol1) 간선 모델링
for start in range(N):
    for i in range(len(G[start])):
        end = G[start][i][0]
        G[start][i][1] -= C[end]

dist = [inf] * N
dist[st] = -C[st]

isCycle = False
for i in range(N):
    for x in range(N):
        if dist[x] == inf:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                if i == N - 1 and P[nx]:
                    isCycle = True

if dist[ed] == inf:
    print("gg")
elif isCycle:
    print("Gee")
else:
    print(-dist[ed])
