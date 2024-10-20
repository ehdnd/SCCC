import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(nums) == 0:
            print(0)
        else:
            print(-heapq.heappop(nums))
    else:
        heapq.heappush(nums, -num)
