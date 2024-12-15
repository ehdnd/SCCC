import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [1] * 1010
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


N = int(input())
nums = list(map(int, input().split()))
print(jud())
