import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def DFS(arr, length):
    if length == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if i in arr:
            continue

        arr.append(i)
        DFS(arr, length + 1)
        arr.pop()


N, M = map(int, input().split())
for i in range(1, N + 1):
    DFS([i], 1)
