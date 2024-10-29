import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(nums):
    cnt = 1
    res = []
    deq = deque()

    for num in nums:
        while 1:
            if not deq or deq[-1] < num:
                deq.append(cnt)
                cnt += 1
                res.append("+")
            elif deq[-1] == num:
                deq.pop()
                res.append("-")
                break
            else:
                return "NO"
    return res


N = int(input())
nums = [int(input()) for _ in range(N)]

res = jud(nums)
if res == "NO":
    print("NO")
else:
    print(*res, sep="\n")
