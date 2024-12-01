import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(res):
    if len(res) == M:
        print(*res)
        return

    for i in range(1, N + 1):
        if res and res[-1] > i:
            continue
        res.append(i)
        jud(res)
        res.pop()

    return


N, M = map(int, input().split())
res = []
jud(res)
