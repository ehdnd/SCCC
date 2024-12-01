import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
inf = int(1e9)

V, E = int(input()), int(input())
G = [[] for _ in range(1010)]
D = [inf] * 1010
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
st, ed = map(int, input().split())

pq = []
heapq.heappush(pq, [0, st])
D[st] = 0

while pq:
    dist, now = heapq.heappop(pq)
    if D[now] < dist:
        continue
    for next, cst in G[now]:
        if D[next] > D[now] + cst:
            D[next] = D[now] + cst
            heapq.heappush(pq, [D[next], next])

print(D[ed])
