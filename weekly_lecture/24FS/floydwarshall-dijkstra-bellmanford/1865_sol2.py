import sys

input = lambda: sys.stdin.readline().rstrip()
inf = int(1e9)

# 멀티 소스 벨만 포트 (multi-source BFS 느낌)
# https://www.acmicpc.net/board/view/72995


def jud():
    isCycle = False
    for i in range(N):
        for x in range(N + 1):
            if dist[x] == inf:
                continue
            for nx, w in G[x]:
                if dist[nx] > dist[x] + w:
                    dist[nx] = dist[x] + w
                    if i == N - 1:
                        isCycle = True

    # 출발지에서 출발지는 사이클이구만
    return "YES" if isCycle else "NO"


# solve2) 멀티소스 벨만 - 포드
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    dist = [0] * 501
    dist[0] = 0
    for _ in range(M):
        S, E, T = map(int, input().split())
        G[S].append([E, T])
        G[E].append([S, T])
    for _ in range(W):
        S, E, T = map(int, input().split())
        G[S].append([E, -T])
    for i in range(1, N + 1):
        G[0].append([i, 0])

    print(jud())
