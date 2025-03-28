import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
dist = [int(1e9)] * (N + 1)
dist[1] = 0
cycle = []

for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append([B, C])

for i in range(N):
    for x in range(1, N + 1):
        if dist[x] >= 1e9:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                if i == N - 1:
                    cycle.append(nx)

if not cycle:
    for i in range(2, N + 1):
        print(dist[i] if dist[i] != 1e9 else -1)
else:
    print(-1)
