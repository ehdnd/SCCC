import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs():
    q = deque()
    q.append(1)
    V[1] = 1
    res = 1

    while q:
        v = q.popleft()
        for nv in G[v]:
            if V[nv]:
                continue
            q.append(nv)
            V[nv] = 1
            res += 1

    return res - 1


N = int(input())
k = int(input())
G = [[] for _ in range(101)]
V = [0] * 101
for i in range(k):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
print(bfs())
