import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def floyd(N: int, R: int) -> list:
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dist[i][i] = 0

    for _ in range(R):
        a, b, l = MIS()
        dist[a][b] = min(dist[a][b], l)
        dist[b][a] = min(dist[b][a], l)

    for x in range(1, N + 1):
        for st in range(1, N + 1):
            for ed in range(1, N + 1):
                dist[st][ed] = min(dist[st][ed], dist[st][x] + dist[x][ed])

    return dist


def find_total(N: int, M: int, dist: list, items: list) -> list:
    start_total = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > M:
                continue
            start_total[i] += items[j]

    return start_total


def solve() -> None:
    N, M, R = MIS()
    items = [0] + list(MIS())
    dist = floyd(N, R)
    start_total = find_total(N, M, dist, items)
    print(max(start_total))
    return


if __name__ == "__main__":
    solve()
