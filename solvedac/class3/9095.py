import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
max_num = max(nums)
F = [0 for i in range(max_num + 1)]
F[2] = 1
F[3] = 3

for i in range(4, max_num + 1):
    for j in range(i - 3, i):
        F[i] += F[j]
        if i - j <= 3 and j < 4:
            F[i] += 1

for num in nums:
    print(F[num])
