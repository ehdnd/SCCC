import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
MAX = 100000


def chk(i: int) -> bool:
    return 0 <= i <= MAX


def bfs(V: list[int], N: int, K: int) -> None:
    q = deque([N])
    V[N] = 1
    while q:
        x = q.popleft()
        if x == K:
            return
        for nx in [x - 1, x + 1, 2 * x]:
            if chk(nx) and not V[nx]:
                V[nx] = V[x] + 1
                q.append(nx)

    return


def find_path(V: list[int], N: int, K: int) -> int:
    P = [0] * (MAX + 1)
    q = deque([K])
    P[K] = 1
    while q:
        x = q.popleft()
        if x == N:
            break

        pxs = [x + 1, x - 1, x // 2] if x % 2 == 0 else [x + 1, x - 1]
        for px in pxs:
            if chk(px) and V[px] + 1 == V[x]:
                if not P[px]:
                    q.append(px)
                P[px] += P[x]

    return P[N]


def solve() -> None:
    N, K = MIS()
    V = [0] * (MAX + 1)
    bfs(V, N, K)
    print(V[K] - 1)
    print(find_path(V, N, K))
    return


if __name__ == "__main__":
    solve()
