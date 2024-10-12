import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
arr = list(map(int, input().split()))
max = -1001

for i in range(N):
    dp = [0] * (N - i)
    dp[0] = arr[i]
    for j in range(N - i):
        dp[j] = dp[j - 1] + arr[i + j]
        if dp[j] > max:
            max = dp[j]

print(max)
