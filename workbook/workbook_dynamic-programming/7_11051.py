import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())


def jud(n, k):
    dp = [0] * 1001
    if n == k:
        return 1

    dp[k] = 1
    for i in range(k + 1, n + 1):
        dp[i] = (dp[i - 1] * i) // (i - k)
    return dp[n]


print(jud(N, K) % 10007)
