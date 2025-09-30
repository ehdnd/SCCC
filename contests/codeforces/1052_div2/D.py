import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve(tt: int) -> None:
    l, r = MIS()
    n = r - l + 1

    p = [0] * n
    currr = r

    while currr >= 0:
        k = currr.bit_length()
        # 꽉 찬
        m = (1 << k) - 1
        st = m ^ currr

        for j in range(st, currr + 1):
            pp = m ^ j
            p[j] = pp

        currr = st - 1

    maxi = 0
    for i in range(n):
        maxi += i | p[i]

    print(maxi)
    print(*p)
    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
