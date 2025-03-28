import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def dijkstra(graph: list[list]) -> list:
    dist = [INF] * (N + 1)
    dist[X] = 0
    pq = []
    heapq.heappush(pq, [0, X])

    while pq:
        w, x = heapq.heappop(pq)
        if dist[x] < w:
            continue

        for nx, cst in graph[x]:
            if dist[nx] > dist[x] + cst:
                dist[nx] = dist[x] + cst
                heapq.heappush(pq, [dist[nx], nx])

    return dist


def jud() -> None:
    fromX = dijkstra(G)
    toX = dijkstra(R)
    res = 0
    for i in range(1, N + 1):
        res = max(res, fromX[i] + toX[i])
    print(res)
    return


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    # X 에서 집으로
    G = [[] for _ in range(N + 1)]
    # X 에서 간선 거꾸로 집으로
    R = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        G[a].append([b, t])
        R[b].append([a, t])

    jud()
