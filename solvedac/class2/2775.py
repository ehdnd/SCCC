import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(K, N):
    dp = [[0 for j in range(N + 1)] for i in range(K + 1)]
    for i in range(N + 1):
        dp[0][i] = i

    for k in range(1, K + 1):
        for n in range(1, N + 1):
            dp[k][n] = sum(dp[k - 1][1 : n + 1])

    print(dp[K][N])

    # for i in dp:
    #     for j in i:
    #         print(j, end=" ")
    #     print()


T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    jud(K, N)
