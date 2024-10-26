import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(N, nums):
    dp = [[nums[i], nums[i]] for i in range(N)]
    for i in range(N):
        now = dp[i][1]
        for j in range(i):
            if dp[i][0] > dp[j][0]:
                dp[i][1] = max(now + dp[j][1], now)
    return max(dp, key=lambda x: x[1])[1]


N = int(input())
nums = list(map(int, input().split()))
print(jud(N, nums))
