import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inf = int(1e9)


def bfs(cycle):
    q = deque(cycle)
    V = [0] * 101
    for node in cycle:
        V[node] = 1

    while q:
        x = q.popleft()
        for nx, _ in G[x]:
            if not V[nx]:
                V[nx] = 1
                q.append(nx)

    return V[N]


def res_print():
    now = N
    res = []
    while now != 1:
        res.append(now)
        now = prev[now]
    res.append(1)
    print(*res[::-1])


N, M = map(int, input().split())
G = [[] for _ in range(101)]
dist = [inf] * (101)
dist[1] = 0
prev = [0] * 101
cycle = []

# 최대 금품을 원하므로 -w 하고 벨만포드
for _ in range(M):
    st, ed, w = map(int, input().split())
    G[st].append([ed, -w])

for i in range(N):
    for x in range(1, N + 1):
        if dist[x] == inf:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                prev[nx] = x
                if i == N - 1:
                    cycle.append(nx)


if cycle and bfs(cycle):
    print(-1)
elif dist[N] == inf:
    print(-1)
else:
    res_print()
