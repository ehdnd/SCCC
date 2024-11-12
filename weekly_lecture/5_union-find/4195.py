import sys

input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if isinstance(S[a], int) and S[a] < 0:
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


T = int(input())
for _ in range(T):
    F = int(input())
    S = {}
    for _ in range(F):
        A, B = input().split()
        if A not in S:
            S[A] = -1
        if B not in S:
            S[B] = -1
        Union(A, B)
        k = Find(A)
        print(-S[k])
