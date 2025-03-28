import sys
import heapq
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


# 노드의 가중치가 간선 가중치의 유일한 결정 요소
def dijkstra(st: int) -> list[int]:
    pq = []
    heapq.heappush(pq, (T[st], st))
    dist = [INF] * (N + 1)
    dist[st] = T[st]

    while pq:
        d, x = heapq.heappop(pq)
        if dist[x] < d:
            continue
        for nx in G[x]:
            w = T[nx]
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                heapq.heappush(pq, (dist[nx], nx))
    return dist


# dist1[4]+dist2[4]−T[4] = T[1]+T[4]+T[8]+T[7]−T[4] = T[1]+T[8]+T[7]
def isUsed(i: int, dist1: list[int], dist2: list[int]) -> bool:
    return dist1[i] + dist2[i] - T[i] == dist2[1]


def make_dag(dist1: list[int], dist2: list[int]) -> tuple[list[int], list[list[int]]]:
    dag = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for u, v in E:
        if isUsed(u, dist1, dist2) and isUsed(v, dist1, dist2):
            if dist1[u] > dist1[v]:
                u, v = v, u
            dag[u].append(v)
            indegree[v] += 1

    return (dag, indegree)


def topological_sorting(dag: list, indegree: list, dist1: list, dist2: list) -> list:
    q = deque()
    for s in range(1, N + 1):
        if isUsed(s, dist1, dist2) and indegree[s] == 0:
            q.append(s)

    res = []
    while q:
        v = q.popleft()
        res.append(v)
        for nx in dag[v]:
            if isUsed(nx, dist1, dist2):
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    q.append(nx)
    return res


def paint(res: list[int]) -> list[int]:
    left_K = K
    ans = [0] * (N + 1)
    if K > N - K:
        # 위상 정렬 -> K개 선택
        for i in res:
            if left_K:
                ans[i] = 1
                left_K -= 1
        for i in range(1, N + 1):
            if not left_K:
                break
            if ans[i] == 0:
                ans[i] = 1
                left_K -= 1
    else:
        # 모든 정점을 선택 -> N-K개를 제외
        for i in range(1, N + 1):
            ans[i] = 1
        p = N - K
        for i in res:
            if p:
                ans[i] = 0
                p -= 1
        for i in range(1, N + 1):
            if p and ans[i] == 1:
                ans[i] = 0
                p -= 1
    return ans[1:]


def solve() -> None:
    for _ in range(M):
        u, v = MIS()
        G[u].append(v)
        G[v].append(u)
        E.append((u, v))

    if N == 2 and K == 1:
        print("impossible")
        return

    dist1 = dijkstra(1)
    dist2 = dijkstra(N)
    dag, indegree = make_dag(dist1, dist2)
    res = topological_sorting(dag, indegree, dist1, dist2)
    ans = paint(res)
    for i in ans:
        print("N" if i else "S", end="")

    return


if __name__ == "__main__":
    N, M, K = MIS()
    T = [0] + list(MIS())
    G = [[] for _ in range(N + 1)]
    E = []
    solve()
