import sys
from math import log

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def print_star(n):
    if n == 1:
        return ["*"]
    p = print_star(n // 3)
    res = []
    for s in p:
        res.append(s * 3)
    for s in p:
        res.append(s + " " * (n // 3) + s)
    for s in p:
        res.append(s * 3)

    return res


def solve() -> None:
    N = II()
    res = print_star(N)
    for r in res:
        print(r)
    return


if __name__ == "__main__":
    solve()
