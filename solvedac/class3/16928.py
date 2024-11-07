import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs():
    q = deque()
    q.append(1)
    V[1] = 1

    while q:
        v = q.popleft()
        if v == 100:
            return V[v] - 1

        for i in range(1, 7):
            nv = v + i
            if nv > 100 or V[nv] >= V[v]:
                continue
            V[nv] = V[v] + 1

            if L[nv]:
                nv = L[nv]
            q.append(nv)
            V[nv] = V[v] + 1


N, M = map(int, input().split())
V = [0] * 101
L = [0] * 101
for _ in range(N + M):
    x, y = map(int, input().split())
    L[x] = y

print(bfs())
