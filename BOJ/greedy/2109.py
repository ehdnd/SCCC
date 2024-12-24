import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
lectures = []
for _ in range(N):
    p, d = map(int, input().split())
    lectures.append((d, p))
lectures.sort(key=lambda x: (x[0], x[1]))

res = 0
temp = []
for i in range(N, 0, -1):
    while lectures and lectures[-1][0] >= i:
        d, p = lectures.pop()
        heapq.heappush(temp, -p)

    if temp:
        res -= heapq.heappop(temp)

print(res)
