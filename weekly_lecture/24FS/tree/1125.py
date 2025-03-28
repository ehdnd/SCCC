import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline().rstrip()


def dfs(v, b):
    for nx in G[v]:
        # 부모 노드 거슬러 올라가기 방지
        if nx != b:
            Par[nx] = v
            # Dep[nx] = Dep[v] + 1
            dfs(nx, v)
    return


N = int(input())
G = [[] for _ in range(101010)]
Par = [0] * 101010
# Dep = [0] * 101010
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dfs(1, -1)
for i in range(2, N + 1):
    print(Par[i])
