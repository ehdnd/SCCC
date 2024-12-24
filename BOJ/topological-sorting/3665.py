import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def make_graph(prev_rank: list[int], changed_rank: list[int], G, idg: list[int], N):
    for i in range(N):
        for j in range(i + 1, N):
            a, b = prev_rank[i], prev_rank[j]
            if (a, b) in changed_rank or (b, a) in changed_rank:
                G[b].append(a)
                idg[a] += 1
            else:
                G[a].append(b)
                idg[b] += 1


def topological_sorting(G: list[list[int]], idg: list[int], N, res: list[int]) -> bool:
    q = deque()
    for i in range(1, N + 1):
        if idg[i] == 0:
            q.append(i)
            res.append(i)

    for _ in range(N):
        if not q:
            return True
        x = q.popleft()
        for nx in G[x]:
            idg[nx] -= 1
            if idg[nx] == 0:
                q.append(nx)
                res.append(nx)
    return False


def Solve() -> None:
    N = II()
    prev_rank = list(MIS())
    M = II()
    changed_rank = set(tuple(MIS()) for _ in range(M))

    G = [[] * (N + 1) for _ in range(N + 1)]
    idg = [0] * (N + 1)
    make_graph(prev_rank, changed_rank, G, idg, N)

    res = []
    isImp = topological_sorting(G, idg, N, res)
    if isImp:
        print("IMPOSSIBLE")
        return

    print(*res)
    return


if __name__ == "__main__":
    T = II()
    for _ in range(T):
        Solve()
