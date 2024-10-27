import sys

input = lambda: sys.stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    res = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        if (x1 <= x3 <= x2 or x2 <= x3 <= x1) and (y1 <= y3 <= y2 or y2 <= y3 <= y1):
            return 2
        else:
            return 0


def jud(L1, L2):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2
    ccw_123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw_124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw_341 = ccw(x1, y1, x3, y3, x4, y4)
    ccw_342 = ccw(x2, y2, x3, y3, x4, y4)
    if ccw_123 == 2 or ccw_124 == 2 or ccw_341 == 2 or ccw_342 == 2:
        return 1
    elif ccw_123 * ccw_124 == 0 or ccw_341 * ccw_342 == 0:
        return 0
    else:
        if ccw_123 * ccw_124 < 0 and ccw_341 * ccw_342 < 0:
            return 1
    return 0


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
print(jud(L1, L2))
