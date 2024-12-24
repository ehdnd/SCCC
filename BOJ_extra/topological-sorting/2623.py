import sys
from collections import deque
from typing import Optional

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def topological_sorting(
    G: list[list[int]], idg: list[int], N: int
) -> Optional[list[int]]:
    res = []
    isN = True
    q = deque()
    for i in range(1, N + 1):
        if idg[i] == 0:
            q.append(i)
            res.append(i)

    for _ in range(N):
        if not q:
            isN = False
            break
        x = q.popleft()
        for nx in G[x]:
            idg[nx] -= 1
            if idg[nx] == 0:
                q.append(nx)
                res.append(nx)

    return res if isN else False


def solve() -> None:
    N, M = MIS()
    G = [[] for _ in range(N + 1)]
    idg = [0] * (N + 1)
    for _ in range(M):
        l = list(MIS())
        for i in range(1, l[0]):
            a, b = l[i], l[i + 1]
            G[a].append(b)
            idg[b] += 1

    res = topological_sorting(G, idg, N)
    print(*res, sep="\n") if res else print(0)
    return


if __name__ == "__main__":
    solve()
