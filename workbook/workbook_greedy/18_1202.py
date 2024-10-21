import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

gems = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(gems, (-(v / m), m, v))

bags = []
for _ in range(M):
    heapq.heappush(bags, -int(input()))

res = 0
for i in range(M):
    bag = -heapq.heappop(bags)
    for j in range(N):
        gem = heapq.heappop(gems)
        if bag >= gem[1]:
            res += gem[2]
            break

print(res)
