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
    dist[1] = 0

    while pq:
        d, x = heapq.heappop(pq)
        if dist[x] < d:
            continue

        for nx in G[x]:
            cst = T[nx]
            if dist[nx] > dist[x] + cst:
                dist[nx] = dist[x] + cst
                heapq.heappush(pq, [dist[nx], nx])

    return dist


# 찾은 최단경로에 포함된 정점 구하기
def bfs(dist: list) -> tuple[list, list]:
    dag = [set() for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    V = [0] * (N + 1)
    q = deque()
    q.append(N)
    V[N] = 1
    while q:
        x = q.popleft()
        for px in G[x]:
            w = T[x]
            if dist[x] == dist[px] + w:
                if x not in dag[px]:
                    dag[px].add(x)
                    indegree[x] += 1
                if not V[px]:
                    V[px] = 1
                    q.append(px)

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
    if flag == 1 and K == 1:
        res = ["S"] * N
        res[1] = "N"
        print(*res, sep="")
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
    flag = 0
    for _ in range(M):
        u, v = map(int, input().split())
        if min(u, v) == 1 and max(u, v) == N:
            flag = 1
        G[u].append(v)
        G[v].append(u)
    jud()
