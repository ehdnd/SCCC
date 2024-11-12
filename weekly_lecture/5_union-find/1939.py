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
S = [-1] * 101010
Bridges = [list(map(int, input().split())) for _ in range(M)]
Bridges.sort(key=lambda x: -x[2])
A, B = map(int, input().split())

res = 0
for Bridge in Bridges:
    a, b, c = Bridge
    Union(a, b)
    res = c
    if Find(A) == Find(B):
        break

print(res)
