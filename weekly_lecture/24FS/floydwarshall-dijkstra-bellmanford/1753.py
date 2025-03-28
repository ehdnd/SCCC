import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
S = int(input())
G = [[] for _ in range(20202)]
D = [1e9] * 20202

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([w, v])

pq = []
heapq.heappush(pq, [0, S])
D[S] = 0

while pq:
    dist, now = heapq.heappop(pq)
    if D[now] < dist:
        continue

    for cst, next in G[now]:
        if D[next] > D[now] + cst:
            D[next] = D[now] + cst
            heapq.heappush(pq, [D[next], next])

for i in range(1, V + 1):
    print(D[i] if D[i] < 1e9 else "INF")
