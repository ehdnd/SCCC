import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def Find(a):
    if S[a] < 0:
        return a
    S[a] = Find(S[a])
    return S[a]


def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a == b:
        return False
    S[a] += S[b]
    S[b] = a
    return True


G = int(input())
P = int(input())
Plane = [int(input()) for _ in range(P)]
S = [-1] * (G + 1)

res = 0
for g in Plane:
    p = Find(g)
    if p == 0:
        break
    res += 1
    Union(p - 1, p)

print(res)
