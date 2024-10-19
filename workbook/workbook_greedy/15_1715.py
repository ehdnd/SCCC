import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

res = 0
while 1:
    if len(cards) <= 1:
        break
    sum = heapq.heappop(cards) + heapq.heappop(cards)
    res += sum
    heapq.heappush(cards, sum)

print(res)
