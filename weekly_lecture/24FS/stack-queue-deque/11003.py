import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(N, L, A):
    deq = deque()
    for i in range(N):
        while deq and deq[0][0] < i - L + 1:
            deq.popleft()
        while deq and deq[-1][1] >= A[i]:
            deq.pop()
        deq.append((i, A[i]))
        print(deq[0][1], end=" ")

    return


N, L = map(int, input().split())
A = list(map(int, input().split()))
jud(N, L, A)
