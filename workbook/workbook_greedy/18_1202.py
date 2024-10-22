import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

gems = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(gems, (m, v))

bags = []
for _ in range(M):
    bags.append(int(input()))
bags.sort()

res = 0
temp = []
for bag in bags:
    for i in range(N):
        if gems:
            gem = heapq.heappop(gems)
            m, v = gem[0], gem[1]
            if m <= bag:
                heapq.heappush(temp, (-v, m))
            else:
                break
        else:
            break

    if temp:
        res -= heapq.heappop(temp)[0]

print(res)
