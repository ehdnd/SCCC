import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def floyd_warshall(N: int, M: int) -> list:
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dist[i][i] = 0

    for _ in range(M):
        a, b = MIS()
        dist[a][b] = 1

    for x in range(1, N + 1):
        for st in range(1, N + 1):
            for ed in range(1, N + 1):
                dist[st][ed] = min(dist[st][ed], dist[st][x] + dist[x][ed])

    return dist


def solve() -> None:
    N, M = MIS()
    dist = floyd_warshall(N, M)
    Q = II()
    for _ in range(Q):
        a, b = MIS()
        if dist[a][b] == INF and dist[b][a] == INF:
            print(0)
        elif dist[b][a] == INF:
            print(-1)
        elif dist[a][b] == INF:
            print(1)

    return


if __name__ == "__main__":
    solve()
