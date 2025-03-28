import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(N, K):
    deq = deque(i for i in range(1, N + 1))
    cnt = 1
    res = []
    while deq:
        if cnt % K == 0:
            r = deq.popleft()
            res.append(r)
        else:
            deq.append(deq.popleft())
        cnt += 1
    return res


N, K = map(int, input().split())
res = jud(N, K)
print("<", end="")
for i in range(N - 1):
    print(res[i], end=", ")
print(res[N - 1], end=">")
