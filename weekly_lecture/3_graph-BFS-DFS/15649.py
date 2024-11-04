import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def DFS(res):
    if len(res) == M:
        print(*res)
        return

    for i in range(1, N + 1):
        if i in res:
            continue

        res.append(i)
        DFS(res)
        res.pop()


N, M = map(int, input().split())
res = []
DFS(res)
