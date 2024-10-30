import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(arr):
    res = []
    deq = deque()
    for num in arr:
        while 1:
            if not deq:
                res.append(-1)
                deq.append(num)
                break

            if deq[-1] > num:
                res.append(deq[-1])
                deq.append(num)
                break
            else:
                deq.pop()

    return res[::-1]


N = int(input())
arr = list(map(int, input().split()))[::-1]
print(*jud(arr))
