import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

gems = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(gems, (m, v))

bags = [int(input()) for _ in range(M)]
bags.sort()

res = 0
temp = []
for bag in bags:
    for i in range(N):
        if gems and gems[0][0] <= bag:
            gem = heapq.heappop(gems)
            m, v = gem[0], gem[1]
            heapq.heappush(temp, -v)
        else:
            break

    if temp:
        res -= heapq.heappop(temp)

print(res)
