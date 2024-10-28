import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud():
    N = int(input())
    deq = deque()
    for _ in range(N):
        d = input()
        if d == "size":
            print(len(deq))
        elif d == "empty":
            if deq:
                print(0)
            else:
                print(1)
        elif d == "front":
            if deq:
                print(deq[0])
            else:
                print(-1)
        elif d == "back":
            if deq:
                print(deq[-1])
            else:
                print(-1)
        elif d == "pop_front":
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        elif d == "pop_back":
            if deq:
                print(deq.pop())
            else:
                print(-1)
        else:
            if d.split()[0] == "push_front":
                deq.appendleft(int(d.split()[1]))
            else:
                deq.append(int(d.split()[1]))
    return


jud()
