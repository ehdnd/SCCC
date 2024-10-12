import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
arr = list(map(int, input().split()))
dp = [[0 for j in range(N + 1)] for i in range(N + 1)]
max = -1001

for start in range(1, N + 1):
    for end in range(start, N + 1):
        dp[start][end] = dp[start][end - 1] + arr[end - 1]
        if dp[start][end] > max:
            max = dp[start][end]

print(max)
