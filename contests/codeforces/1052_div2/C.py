import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve(tt: int) -> None:
    N = II()
    s = input()

    if N > 1 and s[0] == "0" and s[1] == "1":
        print("NO")
        return
    if N > 1 and s[N - 2] == "1" and s[N - 1] == "0":
        print("NO")
        return
    for i in range(1, N - 1):
        if s[i - 1] == "1" and s[i] == "0" and s[i + 1] == "1":
            print("NO")
            return

    print("YES")

    pos = [0] * (N + 1)
    r = N
    ed = N

    while ed >= 1:
        st = ed
        while st > 1 and s[st - 2] == s[ed - 1]:
            st -= 1

        sz = ed - st + 1

        st_r = r - sz + 1
        if s[ed - 1] == "1":
            for k in range(st, ed + 1):
                pos[k] = st_r
                st_r += 1
        else:
            for k in range(ed, st - 1, -1):
                pos[k] = st_r
                st_r += 1

        r -= sz
        ed = st - 1

    p = [0] * (N + 1)
    for k in range(1, N + 1):
        p[pos[k]] = k

    print(*p[1:])

    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
