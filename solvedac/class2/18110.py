import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    if N == 0:
        return 0

    k = round(N * 0.15)
    res = arr[k : N - k]
    s = sum(res)
    b = len(res)

    return round(s / b)


N = int(input())
arr = sorted([int(input()) for _ in range(N)])
print(jud())
