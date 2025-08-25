import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    w, h = MIS()
    p, q = MIS()
    t = II()

    a = t - (w - p)
    b = t - (h - q)

    if (a // w) % 2 == 0:
        x = w - (a % w)
    else:
        x = a % w

    if (b // h) % 2 == 0:
        y = h - (b % h)
    else:
        y = b % h

    print(x, y)

    return


if __name__ == "__main__":
    solve()
