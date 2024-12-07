import sys
from collections import deque
import heapq

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


# 다익스트라로 1->N 최단경로 찾기
def dijkstra() -> list:
    pq = []
    heapq.heappush(pq, [0, 1])
    dist = [INF] * (N + 1)
    dist[1] = T[1]

    while pq:
        d, x = heapq.heappop(pq)
        if dist[x] < d:
            continue

        for nx, cst in G[x]:
            if dist[nx] > dist[x] + cst:
                dist[nx] = dist[x] + cst
                heapq.heappush(pq, [dist[nx], nx])

    return dist


# 찾은 최단경로에 포함된 정점 구하기
def bfs(dist: list) -> tuple[list, list]:
    dag = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for x in range(1, N + 1):
        for nx, w in G[x]:
            if dist[nx] == dist[x] + w:
                dag[x].append(nx)
                indegree[nx] += 1

    return (dag, indegree)


# 최단 경로 만드는 정점 위상정렬
def topological_sorting(dag: list, indegree: list) -> list:
    res = []
    q = deque()
    q.append(1)
    for i in range(N + 1):
        if i != 1 and indegree[i] == 0:
            indegree[i] = -1

    while q:
        v = q.popleft()
        res.append(v)
        for nx in dag[v]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                q.append(nx)

    return res


# 앞 K개 N으로 색칠
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

    dist = dijkstra()
    dag, indegree = bfs(dist)
    res_ts = topological_sorting(dag, indegree)
    res = paint_road(res_ts)
    print(*res, sep="")

    return


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    T = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    R = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append([v, T[v]])
        G[v].append([u, T[u]])
        R[u].append([v, T[u]])
        R[v].append([u, T[v]])
    jud()
