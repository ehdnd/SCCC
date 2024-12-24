import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
M = 10**6


def bfs(N: int, K: int) -> int:
    q = deque()
    q.append(N)
    V[N] = 1

    while q:
        x = q.popleft()
        if x == K:
            return V[K] - 1
        nxs = [x - 1, x + 1, x * 2]
        for nx in nxs:
            if nx < 0 or nx > M or V[nx]:
                continue
            V[nx] = V[x] + 1
            prev[nx] = x
            q.append(nx)

    return


def find_prev(N: int, K: int) -> list:
    res = []
    now = K
    while now != N:
        res.append(now)
        now = prev[now]
    res.append(N)

    return res[::-1]


def solve() -> None:
    N, K = MIS()
    res = bfs(N, K)
    res_prev = find_prev(N, K)
    print(res)
    print(*res_prev)
    return


if __name__ == "__main__":
    V = [0] * (M + 1)
    prev = [0] * (M + 1)
    solve()
