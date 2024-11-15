import sys

input = lambda: sys.stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    res = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0


def isMiddle(L1, L2):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2
    if (
        min(x1, x2) <= max(x3, x4)
        and min(x3, x4) <= max(x1, x2)
        and min(y1, y2) <= max(y3, y4)
        and min(y3, y4) <= max(y1, y2)
    ):
        return True
    else:
        return False


def jud(L1, L2):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2
    ccw_123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw_124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw_341 = ccw(x1, y1, x3, y3, x4, y4)
    ccw_342 = ccw(x2, y2, x3, y3, x4, y4)

    # if ccw_123 == 0 and ccw_124 == 0 and ccw_341 == 0 and ccw_342 == 0:
    if ccw_123 * ccw_124 == 0 and ccw_341 * ccw_342 == 0:
        if isMiddle(L1, L2):
            return 1
        return 0

    if ccw_123 * ccw_124 <= 0 and ccw_341 * ccw_342 <= 0:
        return 1

    return 0


def Find(a):
    if S[a] < 0:
        return a
    S[a] = Find(S[a])
    return S[a]


def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a == b:
        return False
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return True


N = int(input())
S = [-1] * 3001
lines = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if Find(i) == Find(j):
            continue
        L1 = lines[i - 1]
        L2 = lines[j - 1]
        if jud(L1, L2):
            Union(i, j)

cnt = 0
res = 0
for i in range(1, N + 1):
    if S[i] < 0:
        cnt += 1
        res = min(res, S[i])
print(cnt)
print(-res)
