import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
res = 0

for i in range(n):
    res += sum(nums[: i + 1])

print(res)
