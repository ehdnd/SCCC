import sys

input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if S[a] < 0:
        return a
    return Find(S[a])


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


N, M = map(int, input().split())
S = [-1] * 1010101
for _ in range(M):
    q, a, b = map(int, input().split())
    if q == 0:
        Union(a, b)
    else:
        if Find(a) == Find(b):
            print("YES")
        else:
            print("NO")
