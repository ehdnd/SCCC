# for 문으로 나머지가 존재하지 않을떄만 append도 가능

import sys

input = lambda: sys.stdin.readline().rstrip()

nums = []
for _ in range(10):
    nums.append(int(input()))

a = []
for num in nums:
    a.append(num % 42)


print(len(set(a)))
