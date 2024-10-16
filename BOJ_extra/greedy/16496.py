import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = list(input().split())
arr = []
for i in range(N):
    num = nums[i]
    length = len(num)
    num = num + "0" * (10 - length)
    arr.append([int(num), 10 - length])

arr.sort(reverse=True, key=lambda x: (x[0], x[1]))

res = []
for x in arr:
    temp = x[0] // (10 ** x[1])
    res.append(temp)

if set(res) == {0}:
    print(0)
else:
    for x in res:
        print(x, end="")
