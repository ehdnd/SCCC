import sys

input = lambda: sys.stdin.readline().rstrip()


def dfs_pre(v):
    print(v, end="")
    L = G[v][0]
    R = G[v][1]
    if L != ".":
        dfs_pre(L)
    if R != ".":
        dfs_pre(R)


def dfs_in(v):
    L = G[v][0]
    R = G[v][1]
    if L != ".":
        dfs_in(L)
    print(v, end="")
    if R != ".":
        dfs_in(R)


def dfs_post(v):
    L = G[v][0]
    R = G[v][1]
    if L != ".":
        dfs_post(L)
    if R != ".":
        dfs_post(R)
    print(v, end="")


N = int(input())
G = {}
for _ in range(N):
    v, u1, u2 = input().split()
    G[v] = [u1, u2]

dfs_pre("A")
print()
dfs_in("A")
print()
dfs_post("A")
