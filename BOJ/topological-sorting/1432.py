import sys
import heapq
from typing import Optional

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def MakeGraph(N: int, G: list[list[int]], idg: list[int]) -> None:
    r = 1
    for _ in range(N):
        temp_list = list(map(int, input()))
        for i in range(N):
            if temp_list[i]:
                G[i + 1].append(r)
                idg[r] += 1
        r += 1
    return


def TS(N: int, idg: list[int], G: list[list[int]]) -> Optional[dict]:
    res = {i: 0 for i in range(1, N + 1)}
    k = N
    hq = []
    for i in range(N, 0, -1):
        if idg[i] == 0:
            heapq.heappush(hq, -i)

    for _ in range(N):
        if not hq:
            return None
        x = -heapq.heappop(hq)
        res[x] = k
        k -= 1
        for nx in G[x]:
            idg[nx] -= 1
            if idg[nx] == 0:
                heapq.heappush(hq, -nx)

    return res


def solve() -> None:
    N = II()
    G = [[] * (N + 1) for _ in range(N + 1)]
    idg = [0] * (N + 1)
    MakeGraph(N, G, idg)
    res = TS(N, idg, G)

    if res == None:
        print(-1)
        return

    print(*res.values())

    return


if __name__ == "__main__":
    solve()
