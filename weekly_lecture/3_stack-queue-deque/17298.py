import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(N, arr):
    res = deque()
    deq = deque()
    for i in range(N, 0, -1):
        num = arr[i - 1]
        while deq and deq[-1] <= num:
            deq.pop()
        res.appendleft(deq[-1] if deq else -1)
        deq.append(num)

    return res


N = int(input())
arr = list(map(int, input().split()))
print(*jud(N, arr))
