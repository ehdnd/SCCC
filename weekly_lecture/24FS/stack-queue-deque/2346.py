import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(deq):
    res = []
    K = deq.popleft()
    res.append(K[0])

    while deq:
        if K[1] >= 0:
            for _ in range(K[1] - 1):
                deq.append(deq.popleft())
            K = deq.popleft()
        else:
            for _ in range(abs(K[1]) - 1):
                deq.appendleft(deq.pop())
            K = deq.pop()
        res.append(K[0])

    return res


N = int(input())
deq = deque(enumerate(list(map(int, input().split()))))
print(*[x + 1 for x in jud(deq)])
