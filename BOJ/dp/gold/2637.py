import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def ts(G: list[list[int]], N: int, idg: list[int]) -> list[int]:
    Counts = [0] * (N + 1)
    q = deque()
    q.append(N)
    Counts[N] = 1
    while q:
        x = q.popleft()
        for nx, w in G[x]:
            Counts[nx] += Counts[x] * w
            idg[nx] -= 1
            if idg[nx] == 0:
                q.append(nx)

    return Counts


def solve() -> None:
    N, M = II(), II()
    G = [[] for _ in range(N + 1)]
    r_idg = [0] * (N + 1)
    idg = [0] * (N + 1)
    for _ in range(M):
        x, y, k = MIS()
        G[x].append((y, k))
        idg[y] += 1
        r_idg[x] += 1
    Counts = ts(G, N, idg)
    for i in range(1, N):
        if r_idg[i] == 0:
            print(i, Counts[i])
    return


if __name__ == "__main__":
    solve()
