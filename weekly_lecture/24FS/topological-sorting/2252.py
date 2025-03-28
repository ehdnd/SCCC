import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
res = []
q = deque()
cycle = False

for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    G[A].append(B)

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

for _ in range(N):
    if not q:
        cycle = True
        break
    v = q.popleft()
    res.append(v)
    for nx in G[v]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

print(*res)
