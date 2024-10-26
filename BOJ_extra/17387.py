import sys

input = lambda: sys.stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    res = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if res > 0:
        return 1
    elif res == 0:
        return 0
    else:
        return -1


def jud(L1, L2):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2
    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0:
        if ccw(x1, y1, x3, y3, x4, y4) * ccw(x2, y2, x3, y3, x4, y4) <= 0:
            return 1
    return 0


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
print(jud(L1, L2))
