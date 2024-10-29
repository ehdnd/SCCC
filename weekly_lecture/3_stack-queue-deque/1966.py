import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(M, deq):
    cnt = 1
    while 1:
        current = max(deq, key=lambda x: x[1])[1]
        if deq[0][1] == current:
            if deq[0][0] == M:
                return cnt
            deq.popleft()
            cnt += 1
        else:
            deq.append(deq.popleft())


T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    deq = deque(enumerate(list(map(int, input().split()))))
    print(jud(M, deq))
