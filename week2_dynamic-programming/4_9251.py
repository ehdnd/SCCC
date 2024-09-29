import sys

input = lambda: sys.stdin.readline().rstrip()
str1 = input()
str2 = input()
M = len(str1)
N = len(str2)
# N+1개 짜리가 N+1줄 있다
dp = [[0 for j in range(N + 1)] for i in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[M][N])
# for i in dp:
#     for j in i:
#         print(j, end=" ")
#     print()
