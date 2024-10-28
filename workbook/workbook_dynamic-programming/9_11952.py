import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * 1001
for i in range(1, N + 1):
    for j in range(i):
        dp[i] = max(dp[i], p[i], dp[j] + dp[i - j])
print(dp[N])
