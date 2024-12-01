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


def bfs(st):
    q = deque()
    q.append(st)
    V[st] = 1
    while q:
        x = q.popleft()
        for nx, _ in G[x]:
            if nx == N:
                return True
            if V[nx] == 1:
                continue
            q.append(nx)
            V[nx] = 1

    return False


def res_print():
    now = N
    res = []
    while now != 1:
        res.append(now)
        now = prev[now]
    res.append(1)
    print(*res[::-1])


N, M = map(int, input().split())
G = [[] for _ in range(101)]
dist = [inf] * (101)
dist[1] = 0
prev = [0] * 101
cycle = []

# 최대 금품을 원하므로 -w 하고 벨만포드
for _ in range(M):
    st, ed, w = map(int, input().split())
    G[st].append([ed, -w])

for i in range(N):
    for x in range(1, N + 1):
        if dist[x] == inf:
            continue
        for nx, w in G[x]:
            if dist[nx] > dist[x] + w:
                dist[nx] = dist[x] + w
                prev[nx] = x
                if i == N - 1:
                    cycle.append(x)

if cycle:
    for v in cycle:
        V = [0] * (101)
        if bfs(v):
            print(-1)
            break
    else:
        res_print()
elif dist[N] == inf:
    print(-1)
else:
    res_print()
