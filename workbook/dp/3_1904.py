import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

dp = [0] * (N + 1)
dp[1] = 1
if N >= 2:
    dp[2] = 2

    for n in range(3, N + 1):
        dp[n] = dp[n - 2] + dp[n - 1]
        dp[n] = dp[n] % 15746
print(dp[N])
