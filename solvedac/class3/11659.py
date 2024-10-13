import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_arr = [0] * (N + 1)

for i in range(1, N + 1):
    sum_arr[i] = sum_arr[i - 1] + nums[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i - 1])
