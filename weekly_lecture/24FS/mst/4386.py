import sys
import math

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
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return True


N = int(input())
Stars = [list(map(float, input().split())) for _ in range(N)]
S = [-1] * 101

G = []
for i in range(N):
    ax, ay = Stars[i]
    for j in range(i, N):
        bx, by = Stars[j]
        r = (ax - bx) ** 2 + (ay - by) ** 2
        G.append([r, i, j])

G.sort()

res = 0
for w, a, b in G:
    if Union(a, b):
        res += math.sqrt(w)
print(res)
