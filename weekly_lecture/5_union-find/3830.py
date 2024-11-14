import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if S[a] < 0:
        return a
    S[a] = Find(S[a])
    L[a] += L[S[a]]
    return S[a]


def Union(a, b, w):
    if a > b:
        a, b = b, a
        w = -w
    aw, bw = L[a], L[b]
    a, b = Find(a), Find(b)
    if a == b:
        return False
    S[a] += S[b]
    S[b] = a
    L[b] = w + aw - bw
    return True


while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S = [-1] * 1010101
    L = [0] * 1010101
    for _ in range(M):
        query = list(input().split())
        if query[0] == "!":
            a, b, w = map(int, query[1:])
            Union(a, b, w)
        else:
            a, b = map(int, query[1:])
            if Find(a) == Find(b):
                print(L[b] - L[a])
            else:
                print("UNKNOWN")