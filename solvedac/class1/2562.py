# [list].index(n) 으로 n의 인덱스 가져올 수 있다

import sys

input = lambda: sys.stdin.readline().rstrip()

n = 9
nums = []
for i in range(n):
    nums.append(int(input()))

max = max(nums)

for i in range(n):
    if nums[i] == max:
        print(max)
        print(i + 1)
