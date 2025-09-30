import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve(tt: int) -> None:
    N, M = MIS()
    S = []
    P = [[] for _ in range(M + 1)]

    for i in range(N):
        _, *a = [*MIS()]
        S.append(a)
        for x in a:
            P[x].append(i)

    mini = -INF
    for x in range(1, M + 1):
        c = len(P[x])
        if not c:
            print("NO")
            return
        mini = min(mini, c)

    if mini >= 2:
        print("YES")
        return

    must = [0] * N
    for x in range(1, M + 1):
        if len(P[x]) == 1:
            must[P[x][0]] = 1

    cov = [0] * (M + 1)
    for i in range(N):
        if must[i]:
            for x in S[i]:
                cov[x] = 1

    for x in range(1, M + 1):
        if not cov[x]:
            print("YES")
            return

    cnt = sum(1 for i in range(N) if not must[i])
    if cnt >= 2:
        print("YES")
    else:
        print("NO")
    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
