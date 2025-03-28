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
G = [[] for _ in range(N + 1)]
for _ in range(N):
    arr = list(map(int, input().split()))
    v = arr[0]
    for i in range(1, len(arr) - 1):
        if i % 2 != 0:
            G[v].append([arr[i], arr[i + 1]])

V = [-1] * 101010
bfs(1)
sv = V.index(max(V))

V = [-1] * 101010
bfs(sv)
print(max(V))


# for i in range(1, N + 1):
#     print(i, end=" ")
#     for g in G[i]:
#         print(g, end=" ")
#     print()
