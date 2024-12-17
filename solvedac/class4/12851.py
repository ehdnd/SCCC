import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
MAX = 100000


def chk(i: int) -> bool:
    return 0 <= i <= MAX


def bfs(V: list[int], N: int, K: int) -> list[list[int]]:
    G = [[] for _ in range(MAX + 1)]
    q = deque([N])
    V[N] = 1
    while q:
        x = q.popleft()
        for nx in [x - 1, x + 1, 2 * x]:
            if chk(nx):
                if not V[nx] or V[nx] == V[x] + 1:
                    if not V[nx]:
                        q.append(nx)
                    V[nx] = V[x] + 1
                    G[nx].append(x)

    return G


def find_path(G: list[int], N: int, K: int) -> int:
    P = [0] * (MAX + 1)
    q = deque([K])
    P[K] = 1
    while q:
        x = q.popleft()
        for px in G[x]:
            if not P[px]:
                q.append(px)
            P[px] += P[x]

    return P[N]


def solve() -> None:
    N, K = MIS()
    V = [0] * (MAX + 1)
    G = bfs(V, N, K)
    print(V[K] - 1)
    print(find_path(G, N, K))
    return


if __name__ == "__main__":
    solve()
