import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [[0] * 30 for _ in range(30)]
    dp[0][0] = 1

    for i in range(1, 30):
        for j in range(30):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[N - 1][K - 1]


N, K = map(int, input().split())
print(jud())
