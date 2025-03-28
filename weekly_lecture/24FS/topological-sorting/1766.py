import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
MAX = 32001

N, M = map(int, input().split())
G = [[] for _ in range(MAX)]
indegree = [0] * MAX
pq = []
res = []

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

for _ in range(N):
    v = heapq.heappop(pq)
    res.append(v)
    for nx in G[v]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            heapq.heappush(pq, nx)

print(*res)
