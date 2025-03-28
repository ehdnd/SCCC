import sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def bellman_ford() -> bool:
    dist = [INF] * (N + M + 1)
    dist[0] = 0

    for i in range(N + M + 1):
        for x in range(0, N + M + 1):
            if dist[x] == INF:
                continue

            for nx, w in G[x]:
                if dist[nx] > dist[x] + w:
                    dist[nx] = dist[x] + w
                    if i == N + M:
                        return False

    return True


def jud() -> None:
    for _ in range(Q):
        a, b, f, c = input().split()
        a, b, c = int(a), int(b), int(c)
        if f == "<=":
            G[N + b].append([a, c])
        else:
            G[a].append([N + b, -c])

    for i in range(1, N + M + 1):
        G[0].append([i, 0])

    print("Possible" if bellman_ford() else "Impossible")
    return


if __name__ == "__main__":
    while 1:
        N, M, Q = map(int, input().split())
        if N == M == Q == 0:
            break
        G = [[] for _ in range(M + N + 1)]
        jud()
