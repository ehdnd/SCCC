import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
B = [list(map(int, input().split()))[:-1] for _ in range(N)]

G = [[] for _ in range(N + 1)]
cost = [0] * (N + 1)
indegree = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(N):
    cost[i + 1] = B[i][0]
    for j in range(1, len(B[i])):
        G[B[i][j]].append(i + 1)
        indegree[i + 1] += 1

q = deque()
for i in range(N + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = cost[i]

for _ in range(N):
    x = q.popleft()
    for nx in G[x]:
        dp[nx] = max(dp[nx], dp[x] + cost[nx])
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

print(*dp[1:], sep="\n")
