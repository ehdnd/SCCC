import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

dp = [[0 for i in range(2)] for n in range(N + 1)]
dp[1][1] = 1
for n in range(2, N + 1):
    for i in range(2):
        if i == 0:
            dp[n][i] = dp[n - 1][0] + dp[n - 1][1]
        else:
            dp[n][i] = dp[n - 1][0]

res = dp[N][0] + dp[N][1]
print(res)

# # dp 출력
# for i in dp:
#     for j in i:
#         print(j, end=" ")
#     print()
