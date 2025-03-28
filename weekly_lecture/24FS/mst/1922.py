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
        return False
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return True


N, M = int(input()), int(input())
G = [list(map(int, input().split())) for _ in range(M)]
S = [-1] * 1010

G.sort(key=lambda x: x[2])

mst = 0
for a, b, c in G:
    if Union(a, b):
        mst += c
    if (-Find(S[a])) == N:
        break
print(mst)
