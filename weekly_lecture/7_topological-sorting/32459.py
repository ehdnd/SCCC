import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
MAX = 101010

N, M = map(int, input().split())
indegree = [0] * MAX
G = [[] for _ in range(MAX)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    indegree[b] += 1

pq = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

isCycle = False
res = []
for _ in range(N):
    if not pq:
        isCycle = True
        break

    v = heapq.heappop(pq)
    res.append(v)
    for nx in G[v]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            heapq.heappush(pq, nx)

print(*res) if not isCycle else print("IMPOSSIBLE")
