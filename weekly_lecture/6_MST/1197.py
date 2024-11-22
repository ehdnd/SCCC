import sys

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


V, E = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(E)]
S = [-1] * 101010

G.sort(key=lambda x: x[2])

mst = 0
for u, v, w in G:
    if Union(u, v):
        mst += w
    if (-S[Find(u)]) == V:
        break
print(mst)
