import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
tasks = []
for _ in range(N):
    d, w = map(int, input().split())
    tasks.append((d, w))
tasks.sort(reverse=True, key=lambda x: (x[0], x[1]))

date = tasks[0][0]
idx = 0
res = 0
temp = []
while date > 0:
    while idx < N and tasks[idx][0] >= date:
        heapq.heappush(temp, -tasks[idx][1])
        idx += 1
    if temp:
        res -= heapq.heappop(temp)
    date -= 1

print(res)
