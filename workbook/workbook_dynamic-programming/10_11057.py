import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
dp = [[0 for i in range(10)] for j in range(1001)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N + 1):
    for j in range(10):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        dp[i][j] %= 10007

print(sum(dp[N]) % 10007)
