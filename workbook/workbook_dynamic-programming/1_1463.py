import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

F = [0] * (N + 1)
F[0], F[1] = 0, 0

for i in range(2, N + 1):
    nums = []
    idx = []
    if i % 3 == 0:
        nums.append(F[i // 3] + 1)
    if i % 2 == 0:
        nums.append(F[i // 2] + 1)
    nums.append(F[i - 1] + 1)
    F[i] = min(nums)
print(F[N])
