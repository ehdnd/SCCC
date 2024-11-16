import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [-1] * 101010
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, N + 1):
        t, f = 101010, 101010
        if dp[i - 2] != -1:
            t = dp[i - 2]
        if dp[i - 5] != -1:
            f = dp[i - 5]
        dp[i] = min(t, f) + 1
    return dp[N]


N = int(input())
print(jud())
