import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inf = int(1e9)


def bfs():
    q = deque()
    q.append(N)
    prev.append(N)
    V[N] = 1

    while q:
        x = q.popleft()
        for nx, w in G_bfs[x]:
            if dist[nx] == dist[x] - w:
                prev.append(nx)
                q.append(nx)
                V[nx] = 1

    return


N, M = map(int, input().split())
G = [[] for _ in range(101)]
G_bfs = [[] for _ in range(101)]
V = [-1] * 101
dist = [inf] * (101)
dist[1] = 0
prev = []

# 최대 금품을 원하므로 -w 하고 벨만포드
for _ in range(M):
    st, ed, w = map(int, input().split())
    G[st].append([ed, -w])
    G_bfs[ed].append([st, -w])

isCycle = False
for i in range(N):
    for x in range(1, N + 1):
        if dist[x] == inf:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                if i == N - 1:
                    isCycle = True

if isCycle or dist[N] == inf:
    print(-1)
else:
    bfs()
    print(*prev[::-1])
