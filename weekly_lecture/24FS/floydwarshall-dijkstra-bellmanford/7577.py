import sys
from typing import Optional, List, Tuple

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def creat_graph(K: int, N: int) -> List[List[Tuple[int, int]]]:
    G = [[] for _ in range(K + 2)]

    for _ in range(N):
        x, y, r = map(int, input().split())
        G[x - 1].append([y, r])
        G[y].append([x - 1, -r])

    for i in range(0, K + 1):
        G[K + 1].append([i, 0])

    for i in range(1, K + 1):
        G[i - 1].append([i, 1])
        G[i].append([i - 1, 0])

    return G


def bellman_ford(G: List[List[Tuple[int, int]]], K: int) -> Optional[List[int]]:
    dist = [INF] * (K + 2)
    dist[K + 1] = 0

    for i in range(K + 2):
        for x in range(0, K + 2):
            if dist[x] == INF:
                continue
            for nx, w in G[x]:
                if dist[nx] > dist[x] + w:
                    dist[nx] = dist[x] + w
                    if i == K + 1:
                        return None

    return dist


def solve() -> None:
    K, N = map(int, input().split())
    G = creat_graph(K, N)

    res = bellman_ford(G, K)
    if not res:
        print("NONE")
        return

    for i in range(1, K + 1):
        if res[i] - res[i - 1] == 1:
            print("#", end="")
        else:
            print("-", end="")
    return


if __name__ == "__main__":
    solve()
