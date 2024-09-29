import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = list(map(int, input().split()))


def jud(nums, N):
    cnt = 0
    max_num = max(nums)
    for num in nums:
        cnt += num / max_num * 100
    return cnt / N


print(jud(nums, N))
