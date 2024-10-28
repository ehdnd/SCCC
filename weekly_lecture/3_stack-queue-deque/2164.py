import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(N):
    deq = deque()
    for i in range(1, N + 1):
        deq.append(i)
    if N == 1:
        return 1
    while 1:
        deq.popleft()
        if len(deq) == 1:
            return deq.popleft()
        a = deq.popleft()
        deq.append(a)


N = int(input())
print(jud(N))
