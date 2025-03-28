import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(N):
    dp = [100001] * (N + 1)
    dp[0] = 0

    for s in range(1, N + 1):
        e = 1
        while e * e <= s:
            dp[s] = min(dp[s], dp[s - e * e] + 1)
            e += 1
    return dp[N]


N = int(input())
print(jud(N))
