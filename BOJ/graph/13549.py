import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)
M = int(1e5)


def bfs(st: int, K: int) -> int:
    q = deque()
    q.append(st)
    L[st] = 0
    while q:
        x = q.popleft()
        if x == K:
            return L[K]

        nxs = [(x * 2, 0), (x - 1, 1), (x + 1, 1)]
        for nx, l in nxs:
            if nx < 0 or nx > M or L[nx] <= L[x] + l:
                continue
            L[nx] = L[x] + l
            q.appendleft(nx) if l == 0 else q.append(nx)

    return


def solve() -> None:
    N, K = MIS()
    res = bfs(N, K)
    print(res)
    return


if __name__ == "__main__":
    L = [INF] * (M + 1)
    solve()
