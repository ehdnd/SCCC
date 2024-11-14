import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if S[a] < 0:
        return a
    p = Find(S[a])
    L[a] += L[p]
    S[a] = p
    return S[a]


def Union(a, b, w):
    aw, bw = L[a], L[b]
    a = Find(a)
    b = Find(b)
    if a == b:
        return False
    S[a] += S[b]
    S[b] = a
    L[b] = w + aw - bw
    return True


while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    S = [-1] * 1010101
    L = [0] * 1010101
    for _ in range(M):
        query = list(input().split())
        if query[0] == "!":
            q, a, b, w = query
            Union(int(a), int(b), int(w))
        else:
            q, a, b = query
            a, b = int(a), int(b)
            if Find(a) == Find(b):
                print(L[b] - L[a])
            else:
                print("UNKNOWN")
