import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def dfs(v, prevw):
    for node, w in G[v]:
        if V[node] == -1:
            V[node] = w + prevw
            dfs(node, V[node])


N = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v, u, w = map(int, input().split())
    G[v].append([u, w])
    G[u].append([v, w])

V = [-1] * (N + 1)
V[1] = 0
dfs(1, 0)
start_v = V.index(max(V))

V = [-1] * (N + 1)
V[start_v] = 0
dfs(start_v, 0)

print(max(V))
