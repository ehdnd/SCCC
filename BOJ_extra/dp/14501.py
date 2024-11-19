import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [0] * 1010
    for i in range(N, 0, -1):
        t = Tasks[i][0]
        p = Tasks[i][1]
        if i + t - 1 <= N:
            dp[i] = max(dp[i + 1], p + dp[i + t])
        else:
            dp[i] = dp[i + 1]

    return dp[1]


N = int(input())
Tasks = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
print(jud())
