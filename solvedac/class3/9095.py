import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
max_num = max(nums)
F = [0 for i in range(max_num + 1)]
F[1] = 1
F[2] = 2
F[3] = 4

for i in range(4, max_num + 1):
    F[i] = F[i - 1] + F[i - 2] + F[i - 3]

for num in nums:
    print(F[num])
