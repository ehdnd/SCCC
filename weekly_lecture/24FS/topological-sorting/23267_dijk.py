import sys
from collections import deque
import heapq

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def dijkstra(st: int, r: bool) -> list:
    pq = []
    heapq.heappush(pq, [T[st], st])
    dist = [INF] * (N + 1)
    dist[st] = T[st]

    while pq:
        d, x = heapq.heappop(pq)
        if dist[x] < d:
            continue

        for nx in G[x]:
            cst = T[x] if r else T[nx]
            if dist[nx] > dist[x] + cst:
                dist[nx] = dist[x] + cst
                heapq.heappush(pq, [dist[nx], nx])

    return dist


def paint_road(res_ts: list) -> list:
    res = ["S" for _ in range(N + 1)]
    used_N = 0
    for i in res_ts:
        if used_N == K:
            break
        res[i] = "N"
        used_N += 1

    for i in range(1, N + 1):
        if used_N == K:
            break
        if res[i] != "N":
            res[i] = "N"
            used_N += 1

    return res[1:]


def jud() -> None:
    if N == 2 and K == 1:
        print("impossible")
        return
    if flag == 1 and K == 1:
        res = ["S"] * N
        res[1] = "N"
        print(*res, sep="")
        return

    dist_1 = dijkstra(1, 0)
    dist_N = dijkstra(N, 1)

    d = dist_1[N] + dist_N[N]
    Nodes = [0] * (N + 1)
    for i in range(1, N + 1):
        if dist_1[i] + dist_N[i] == d:
            Nodes[i] = 1
    dist = list(enumerate(dist_1))
    dist.sort(key=lambda x: x[1])

    res_ts = []
    for node, _ in dist:
        if Nodes[node]:
            res_ts.append(node)
    res = paint_road(res_ts)
    print(*res, sep="")

    return


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    T = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    flag = 0
    for _ in range(M):
        u, v = map(int, input().split())
        if min(u, v) == 1 and max(u, v) == N:
            flag = 1
        G[u].append(v)
        G[v].append(u)
    jud()
