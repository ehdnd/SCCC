import sys
from collections import deque

inf = int(1e9)
input = lambda: sys.stdin.readline().rstrip()


def bfs(v):
    q = deque()
    q.append(v)
    V = [0] * (N + 1)
    V[v] = 1

    res = 0
    while q:
        x = q.popleft()
        for pv, w in R[x]:
            if dist[x] == dist[pv] + w:
                res += 1
                if not V[pv]:
                    V[pv] = 1
                    q.append(pv)

    return res


N, M = int(input()), int(input())
G = [[] for _ in range(N + 1)]
R = [[] for _ in range(N + 1)]

indegree = [0] * (N + 1)
for _ in range(M):
    a, b, w = map(int, input().split())
    G[a].append([b, w])
    R[b].append([a, w])
    indegree[b] += 1

st, ed = map(int, input().split())

q = deque()
for i in range(N + 1):
    if indegree[i] == 0:
        q.append(i)

dist = [0] * (N + 1)
for _ in range(N):
    x = q.popleft()
    for nx, w in G[x]:
        indegree[nx] -= 1
        dist[nx] = max(dist[nx], dist[x] + w)
        if indegree[nx] == 0:
            q.append(nx)


print(dist[ed])
print(bfs(ed))
