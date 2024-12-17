import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def folyd_warshall(G: list[list[int]], N: int) -> None:
    for x in range(1, N + 1):
        for st in range(1, N + 1):
            for ed in range(1, N + 1):
                G[st][ed] = min(G[st][ed], G[st][x] + G[x][ed])
    return


def find_b(G: list[list[int]], row: int, N: int):
    res = 0
    for j in range(1, N + 1):
        res += G[row][j]
    return res


def solve() -> None:
    N, M = MIS()
    G = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        G[i][i] = 0
    for _ in range(M):
        a, b = MIS()
        G[a][b] = 1
        G[b][a] = 1
    folyd_warshall(G, N)

    res = INF
    p = None
    for i in range(1, N + 1):
        k = find_b(G, i, N)
        if res > k:
            res = k
            p = i
    print(p)

    return


if __name__ == "__main__":
    solve()
