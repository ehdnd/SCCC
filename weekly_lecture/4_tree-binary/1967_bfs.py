import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(v):
    q = deque()
    q.append(v)
    V[v] = 0

    while q:
        x = q.popleft()
        for nv, nw in G[x]:
            if V[nv] != -1:
                continue
            V[nv] = V[x] + nw
            q.append(nv)

    return


N = int(input())
G = [[] for _ in range(10101)]
for _ in range(N - 1):
    v, u, w = map(int, input().split())
    G[v].append([u, w])
    G[u].append([v, w])

V = [-1] * (10101)
bfs(1)
sv = V.index(max(V))

V = [-1] * 10101
bfs(sv)
print(max(V))
