import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(N):
    deq = deque(i for i in range(1, N + 1))
    while len(deq) > 1:
        deq.popleft()
        a = deq.popleft()
        deq.append(a)
    return deq[0]


N = int(input())
print(jud(N))
