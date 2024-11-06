import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    V = [1] * (M + 1)

    m = int(M**0.5)
    for i in range(2, m + 1):
        if V[i]:
            for j in range(i + i, M + 1, i):
                V[j] = 0

    for i in range(2, M + 1):
        if not V[i] or i < N:
            continue
        print(i)


N, M = map(int, input().split())
jud()
