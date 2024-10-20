import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    if num == 0:
        print(heapq.heappop(nums)[1] if len(nums) > 0 else 0)
    else:
        heapq.heappush(nums, (abs(num), num))
