import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [0] * 81
    dp[1] = 4
    dp[2] = 6
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]


N = int(input())
print(jud())
