import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N, M = MIS()
    G = [[] for _ in range(N + 1)]
    idg = [0] * (N + 1)
    for _ in range(M):
        a, b = MIS()
        G[a].append(b)
        idg[b] += 1

    q = deque()
    res = [0] * (N + 1)
    for i in range(1, N + 1):
        if idg[i] == 0:
            q.append(i)
            res[i] = 1

    while q:
        x = q.popleft()
        for nx in G[x]:
            idg[nx] -= 1
            if idg[nx] == 0:
                q.append(nx)
                res[nx] = res[x] + 1

    print(*res[1:])

    return


if __name__ == "__main__":
    solve()
