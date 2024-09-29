import sys

input = lambda: sys.stdin.readline().rstrip()
N, M, K = map(int, input().split())
dp = [[0 for col in range(M)] for row in range(N)]

for col in range(M):
    dp[0][col] = 1
for row in range(N):
    dp[row][0] = 1

# dp[N][M] = dp[N - 1][M] + dp[N][M - 1]
for n in range(1, N):
    for m in range(1, M):
        dp[n][m] = dp[n - 1][m] + dp[n][m - 1]

if K == 0:
    print(dp[N - 1][M - 1])

else:
    temp_M = K % M
    if temp_M != 0:
        K_M = temp_M
        K_N = K // M + 1
    else:
        K_M = M
        K_N = K // M
    K_M -= 1
    K_N -= 1

    # print(K_N, K_M)

    res = dp[K_N][K_M] * dp[N - K_N - 1][M - K_M - 1]
    print(res)

# dp[K_row][K_col] = -1

# for i in dp:
#     for j in i:
#         print(j, end=" ")
#     print()
