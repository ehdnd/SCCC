import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def floyd_warshall(N: int, M: int) -> list:
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dist[i][i] = 0
    # 작 -> 큰 그래프 간선
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
    res = 0
    for i in range(1, N + 1):
        b_cnt, s_cnt = 0, 0
        for j in range(1, N + 1):
            if i == j:
                continue

            if dist[i][j] != INF:
                b_cnt += 1
            if dist[j][i] != INF:
                s_cnt += 1

        if b_cnt + s_cnt == N - 1:
            res += 1

    print(res)
    return


if __name__ == "__main__":
    solve()
