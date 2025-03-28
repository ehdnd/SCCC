import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def dijkstra() -> tuple[list, list]:
    dist = [INF] * (N + 1)
    dist[st] = 0
    pq = []
    heapq.heappush(pq, [0, st])
    prev = [0] * (N + 1)

    while pq:
        d, x = heapq.heappop(pq)
        if dist[x] < d:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                prev[nx] = x
                heapq.heappush(pq, [dist[nx], nx])

    return (dist, prev)


# prev 아무거나 출력가능하네 -> len(prev)
def find_edges(prev: list) -> list:
    path = []
    cur = ed
    while cur:
        path.append(cur)
        cur = prev[cur]

    return path


def jud() -> None:
    dist, prev = dijkstra()
    path = find_edges(prev)

    print(dist[ed])
    print(len(path))
    print(*path[::-1])
    return


if __name__ == "__main__":
    N, M = int(input()), int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        G[a].append([b, w])
    st, ed = map(int, input().split())

    jud()
