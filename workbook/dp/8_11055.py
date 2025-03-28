import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(N, nums):
    dp = [nums[i] for i in range(N)]
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], nums[i] + dp[j])
    return max(dp)


N = int(input())
nums = list(map(int, input().split()))
print(jud(N, nums))
