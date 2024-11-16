import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [[0, 0] for _ in range(46)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, K + 1):
        dp[i] = [dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]]

    return dp[K]


K = int(input())
print(*jud())
