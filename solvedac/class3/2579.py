import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
stairs = [0] * 301
for i in range(1, N + 1):
    stairs[i] = int(input())

dp = [[0, 0] for _ in range(301)]
dp[1][0] = stairs[1]
dp[1][1] = 0
dp[2][0] = dp[1][0] + stairs[2]
dp[2][1] = stairs[2]

for i in range(3, N + 1):
    dp[i][0] = dp[i - 1][1] + stairs[i]
    dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + stairs[i]

print(max(dp[N][0], dp[N][1]))
