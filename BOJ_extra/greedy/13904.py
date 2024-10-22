import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
tasks = []
for _ in range(N):
    d, w = map(int, input().split())
    heapq.heappush(tasks, (-d, -w))

res = 0
date = -tasks[0][0]
temp = []
while tasks and date > 0:
    for task in tasks:
        if -task[0] >= date:
            d, w = heapq.heappop(tasks)
            heapq.heappush(temp, (w, d))
        else:
            break
    if temp:
        res -= heapq.heappop(temp)[0]
    date -= 1

print(res)
