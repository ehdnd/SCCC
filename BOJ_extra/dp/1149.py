import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [[0, 0, 0] for _ in range(1010)]
    for i in range(1, N + 1):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + Houses[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + Houses[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + Houses[i][2]

    return min(dp[N])


N = int(input())
Houses = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
print(jud())
