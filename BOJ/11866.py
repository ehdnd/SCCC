import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(N, K):
    deq = deque(i for i in range(1, N + 1))
    res = []
    while deq:
        for _ in range(K - 1):
            deq.append(deq.popleft())
        res.append(deq.popleft())
    return res


N, K = map(int, input().split())
res = jud(N, K)
print("<" + ", ".join(map(str, res)) + ">")
