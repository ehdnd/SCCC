import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(N, L, A):
    deq = deque()
    res = []
    for i in range(N):
        while deq:
            if deq[0][0] < i - L + 1:
                deq.popleft()
            else:
                break
        while deq:
            if deq[-1][1] >= A[i][1]:
                deq.pop()
            else:
                break
        deq.append(A[i])
        res.append(deq[0][1])

    return res


N, L = map(int, input().split())
A = list(enumerate(list(map(int, input().split()))))
print(*jud(N, L, A))
