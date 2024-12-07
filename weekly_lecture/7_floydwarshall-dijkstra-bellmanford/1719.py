import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def folyd_warshall(N: int, M: int) -> list:
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    table = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dist[i][i] = 0

    for _ in range(M):
        a, b, w = MIS()
        dist[a][b] = min(dist[a][b], w)
        dist[b][a] = min(dist[b][a], w)
        table[a][b] = b
        table[b][a] = a

    for x in range(1, N + 1):
        for st in range(1, N + 1):
            for ed in range(1, N + 1):
                if dist[st][ed] > dist[st][x] + dist[x][ed]:
                    dist[st][ed] = dist[st][x] + dist[x][ed]
                    table[st][ed] = table[st][x]

    return table


def solve() -> None:
    N, M = MIS()
    table = folyd_warshall(N, M)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                print("-", end=" ")
                continue
            print(table[i][j], end=" ")
        print()

    return


if __name__ == "__main__":
    solve()
