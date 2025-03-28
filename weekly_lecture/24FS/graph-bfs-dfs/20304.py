import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs():
    q = deque()
    for p in P:
        q.append(p)
        V[p] = 1

    while q:
        v = q.popleft()
        for i in range(21):
            nv = v ^ (1 << i)
            if nv < 0 or nv > N or V[nv]:
                continue
            q.append(nv)
            V[nv] = V[v] + 1

    return max(V) - 1


N = int(input())
M = int(input())
P = list(map(int, input().split()))
V = [0] * 1010101
print(bfs())
