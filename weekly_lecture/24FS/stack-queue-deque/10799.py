import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(arr):
    isTrue = True
    cnt = 0
    deq = deque()

    for a in arr:
        if a == "(":
            deq.append(a)
            isTrue = True
        else:
            if isTrue:
                deq.pop()
                cnt += len(deq)
                isTrue = False
            else:
                deq.pop()
                cnt += 1

    return cnt


arr = input()
print(jud(arr))
