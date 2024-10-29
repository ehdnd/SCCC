import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def jud(M, deq):
    cnt = 1
    while 1:
        current = max(deq)[0]
        if deq[0][0] == current:
            if deq[0][1] == M:
                return cnt
            deq.popleft()
            cnt += 1
        else:
            deq.append(deq.popleft())


T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    deq = deque()
    for j in range(N):
        deq.append((arr[j], j))
    print(jud(M, deq))
