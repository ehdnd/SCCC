import sys

input = lambda: sys.stdin.readline().rstrip()


def round(N):
    temp = N * 0.15
    if temp - int(temp) < 0.5:
        return int(temp)
    else:
        return int(temp) + 1


def jud():
    if N == 0:
        return 0

    k = round(N)
    res = arr[k : N - k]
    s = sum(res)
    b = len(res)

    return (s + b // 2) // b


N = int(input())
arr = sorted([int(input()) for _ in range(N)])
print(jud())
