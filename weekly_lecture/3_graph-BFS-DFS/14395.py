import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(s, t, V):
    if t == s:
        return 0
    elif t == 1:
        return "/"

    q = deque()
    q.append([s, ""])
    V.add(s)

    while q:
        x, string = q.popleft()
        if x == t:
            return string

        dx = [x**2, x * 2, 0, 1]
        dr = ["*", "+", "-", "/"]
        for i in range(4):
            nx = dx[i]
            nr = dr[i]
            if nx < 0 or nx > t or nx in V:
                continue
            q.append([nx, string + nr])
            V.add(nx)

    return -1


s, t = map(int, input().split())
V = set()
print(BFS(s, t, V))
