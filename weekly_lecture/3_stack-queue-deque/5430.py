import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def drop(isForward, deq):
    if isForward:
        deq.popleft()
    else:
        deq.pop()
    return deq


def jud(deq, p):
    isForward = True
    for f in p:
        if f == "R":
            isForward = not isForward
        else:
            if deq:
                deq = drop(isForward, deq)
            else:
                return -1
    if not isForward:
        deq.reverse()
    return deq


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if n == 0:
        deq = input()
        deq = deque()
    # elif n == 1:
    #     deq = deque([int(input().strip("[]"))])
    # else:
    #     deq = deque(map(int, input().strip("[]").split(",")))
    else:
        deq = deque(input()[1:-1].split(","))

    res = jud(deq, p)
    if res == -1:
        print("error")
    else:
        # print(f"[{','.join(map(str, res))}]")
        print(f"[{','.join(res)}]")
