import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve(tt: int) -> None:
    N = II()
    s = input()
    ss = "".join(sorted(s))

    if s == ss:
        print(0)
        return

    z = s.count("0")
    m = 0
    for i in range(z):
        if s[i] == "1":
            m += 1
    print(m)

    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
