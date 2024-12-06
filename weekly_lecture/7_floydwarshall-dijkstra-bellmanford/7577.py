import sys
from typing import Optional

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)


def bellman_ford() -> Optional[list[int]]:
    dist = [INF] * (K + 2)
    dist[K + 1] = 0

    for i in range(K + 2):
        isChanged = False
        for x in range(0, K + 2):
            if dist[x] == INF:
                continue

            for nx, w in G[x]:
                if dist[nx] > dist[x] + w:
                    dist[nx] = dist[x] + w
                    if i == K + 1:
                        isChanged = True
    if isChanged:
        return None
    return dist


def jud() -> None:
    # 모든 노드에 대한 새로운 시작점을 K+1 에 만들어주자
    for i in range(0, K + 1):
        G[K + 1].append([i, 0])

    # 0 <= (1, 2] <= 1
    for i in range(1, K + 1):
        G[i - 1].append([i, 1])
        G[i].append([i - 1, 0])

    res = bellman_ford()
    if not res:
        print("NONE")
        return

    for i in range(1, K + 1):
        if res[i] - res[i - 1] == 1:
            print("#", end="")
        else:
            print("-", end="")
    return


# 단순연립부등식을 벨만포드로 모델링
# difference constraints and shortest paths
# 부등식을 그래프로 표현만 하면 알아서 알맞은 해를 찾아준다
if __name__ == "__main__":
    K, N = map(int, input().split())
    G = [[] for _ in range(K + 2)]
    for _ in range(N):
        x, y, r = map(int, input().split())
        # (x-1, y] == r 은
        # (x-1, y] <= r / (x-1, y] >= r 로 거리 제약 조건
        G[x - 1].append([y, r])
        G[y].append([x - 1, -r])

    jud()
