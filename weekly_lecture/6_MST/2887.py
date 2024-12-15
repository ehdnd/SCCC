import sys

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


def make_edges_by_axis(Nodes: list, axis: int, N: int) -> list[int, int, int]:
    Edges_sub = []
    Nodes.sort(key=lambda x: x[1][axis])
    for i in range(N - 1):
        a, cor_a = Nodes[i]
        b, cor_b = Nodes[i + 1]
        Edges_sub.append([abs(cor_a[axis] - cor_b[axis]), a, b])
    return Edges_sub


def make_edges(N: int, Nodes: list) -> list[int, int, int]:
    Edges = []
    for axis in range(3):
        Edges += make_edges_by_axis(Nodes, axis, N)
    return Edges


def solve() -> None:
    N = II()
    Nodes = [list(MIS()) for _ in range(N)]
    Nodes = list(enumerate(Nodes, start=1))
    Edges = make_edges(N, Nodes)
    Edges.sort()
    res = 0
    for r, a, b in Edges:
        if Union(a, b):
            res += r
        if -S[Find(a)] == N:
            break
    print(res)
    return


if __name__ == "__main__":
    S = [-1] * 101010
    solve()
