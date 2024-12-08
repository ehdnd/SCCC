import sys
from math import sqrt

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def Find(a):
    if S[a] < 0:
        return a
    S[a] = Find(S[a])
    return S[a]


def Union(a, b):
    a, b = Find(a), Find(b)
    if a == b:
        return False
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return True


def make_edges(Nodes: list, N: int) -> list:
    Edges = []
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            x1, y1 = Nodes[i]
            x2, y2 = Nodes[j]
            r = (x1 - x2) ** 2 + (y1 - y2) ** 2
            Edges.append([r, i, j])
    Edges.sort()
    return Edges


def solve() -> None:
    N, M = MIS()
    Nodes = [[0, 0]] + [list(MIS()) for _ in range(N)]
    for _ in range(M):
        a, b = MIS()
        Union(a, b)
    Edges = make_edges(Nodes, N)

    res = 0
    for r, a, b in Edges:
        if Union(a, b):
            res += sqrt(r)
        if -S[Find(a)] == N:
            print(f"{res:.2f}")
            return

    return


if __name__ == "__main__":
    S = [-1] * 1010
    solve()
