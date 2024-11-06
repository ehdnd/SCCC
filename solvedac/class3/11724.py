import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(v):
    q = deque()
    q.append(v)
    V[v] = 1

    while q:
        x = q.popleft()
        for nv in G[x]:
            if V[nv]:
                continue
            q.append(nv)
            V[nv] = 1
    return


N, M = map(int, input().split())
G = [[] for _ in range(1001)]
V = [0] * 1001
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

cnt = 0
for i in range(1, N + 1):
    if V[i]:
        continue
    bfs(i)
    cnt += 1
print(cnt)
