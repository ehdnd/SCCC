import sys

sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()


# Siz v에 속한 정점의 개수를 저장하자
def dfs(v, b):
    Siz[v] = 1
    for nx in G[v]:
        if nx != b:
            dfs(nx, v)
        Siz[v] += Siz[nx]


N, R, Q = map(int, input().split())
G = [[] for _ in range(101010)]
Siz = [0] * (101010)
for i in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dfs(R, -1)
for i in range(Q):
    print(Siz[int(input())])
