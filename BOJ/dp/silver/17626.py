import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [50001] * 50001
    dp[0] = 0

    dp[1] = 1
    for i in range(2, N + 1):
        e = 1
        while e * e <= i:
            dp[i] = min(dp[i], 1 + dp[i - e * e])
            e += 1

    return dp[N]


N = int(input())
print(jud())
