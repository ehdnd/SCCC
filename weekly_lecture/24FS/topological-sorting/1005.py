import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud():
    for _ in range(N):
        v = q.popleft()
        for nx in G[v]:
            dp[nx] = max(dp[nx], dp[v] + cost[nx])
            indegree[nx] -= 1
            if indegree[nx] == 0:
                q.append(nx)
    return dp[w]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    G = [[] for _ in range(1010)]
    cost = [0] + list(map(int, input().split()))
    indegree = [0] * 1010
    dp = [0] * 1010

    q = deque()
    for _ in range(K):
        x, y = map(int, input().split())
        G[x].append(y)
        indegree[y] += 1

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    w = int(input())
    print(jud())
