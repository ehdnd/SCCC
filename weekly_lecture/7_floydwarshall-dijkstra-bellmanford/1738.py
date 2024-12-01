import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inf = int(1e9)

# 문제1)
# 음의 사이클이 존재하는지..
# 근데 이 사이클이 목적지까지 도달하는데 영향이 없다면?

# 문제2)
# 경로 역추적은 어떻게 진행할 것인가?
# prev 배열을 선언해서 가중치 업데이트 될 떄마다 갱신하자

# 엥?
# 그럼 prev 배열로 bfs 는 어디서 사용하던것인지?


def bfs():
    q = deque()
    q.append(N)
    prev.append(N)
    V[N] = 1

    while q:
        x = q.popleft()
        for st in range(1, N + 1):
            for nx, w in G[st]:
                if dist[nx] == dist[x] - w:
                    prev.append(nx)
                    q.append(nx)
                    V[nx] = 1

    return


N, M = map(int, input().split())
G = [[] for _ in range(101)]
V = [-1] * 101
dist = [inf] * (101)
dist[1] = 0

# 최대 금품을 원하므로 -w 하고 벨만포드
for _ in range(M):
    st, ed, w = map(int, input().split())
    G[st].append([ed, -w])

isCycle = False
for i in range(N):
    for x in range(1, N + 1):
        if dist[x] == inf:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                if i == N - 1:
                    isCycle = True

if isCycle or dist[N] == inf:
    print(-1)
else:
    bfs()
    print(*prev[::-1])
