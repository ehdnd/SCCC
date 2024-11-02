import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(N, K):
    q = deque()
    q.append(N)
    visit[N] = 1

    while q:
        v = q.popleft()
        if v == K:
            return visit[v]
        move = [v - 1, v + 1, 2 * v]
        for m in move:
            if m > 100000 or m < 0 or visit[m]:
                continue
            q.append(m)
            visit[m] = visit[v] + 1


N, K = map(int, input().split())
visit = [0] * (100001)
print(BFS(N, K) - 1)
