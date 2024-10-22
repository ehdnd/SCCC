import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
lectures = []
for _ in range(N):
    p, d = map(int, input().split())
    lectures.append((d, p))
lectures.sort(reverse=True, key=lambda x: (x[0], x[1]))

res = 0
temp = []
max_date = lectures[0][0]
for i in range(max_date, 0, -1):
    while lectures and lectures[0][0] >= i:
        d, p = lectures.pop(0)
        heapq.heappush(temp, -p)

    if temp:
        res -= heapq.heappop(temp)

print(res)
