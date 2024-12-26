import sys

input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if S[a] < 0:
        return a
    S[a] = Find(S[a])
    return S[a]


def Union(a, b):
    a, b = Find(a), Find(b)
    if a == b:
        return 0
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return 1


while 1:
    M, N = map(int, input().split())
    if N == 0 and M == 0:
        break

    G = [list(map(int, input().split())) for _ in range(N)]
    S = [-1] * 200000

    G.sort(key=lambda x: x[-1])

    res = 0
    total = 0
    for x, y, z in G:
        total += z
        if Union(x, y):
            res += z
        # if -S[Find(x)] == M:
        #     break
    print(total - res)
