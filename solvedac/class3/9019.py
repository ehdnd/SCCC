import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs():
    q = deque()
    q.append(A)
    V[A] = 1

    while q:
        x = q.popleft()
        if x == B:
            return G[B]

        m = ["D", "S", "L", "R"]
        dx = P[x]
        for i in range(4):
            nx = dx[i]
            if nx < 0 or nx > 10000 or V[nx]:
                continue
            q.append(nx)
            V[nx] = 1
            G[nx] = G[x] + [m[i]]
    return


T = int(input())

P = [[] for _ in range(10000)]
for x in range(10000):
    d1 = x // 1000
    d2 = x % 1000 // 100
    d3 = x % 100 // 10
    d4 = x % 10
    dx = [
        2 * x % 10000,
        x - 1 if x != 0 else 9999,
        ((d2 * 10 + d3) * 10 + d4) * 10 + d1,
        ((d4 * 10 + d1) * 10 + d2) * 10 + d3,
    ]
    P[x] = dx

for _ in range(T):
    A, B = map(int, input().split())
    G = [[] for _ in range(10000)]
    V = [0] * 10000
    print(*bfs(), sep="")
