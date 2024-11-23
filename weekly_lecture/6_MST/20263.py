import sys

input = lambda: sys.stdin.readline().rstrip()


def Find(S, a):
    if S[a] < 0:
        return a
    S[a] = Find(S, S[a])
    return S[a]


def Union(S, a, b):
    a, b = Find(S, a), Find(S, b)
    if a == b:
        return 0
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return 1


def mst(S, mid):
    for a, b, w in G:
        if w < mid:
            continue
        Union(S, a, b)
        if -S[Find(S, a)] == N:
            return 1
    return 0


def binary_search(left, right):
    while 1:
        if right < left:
            return right

        mid = (left + right) // 2
        S = [-1] * 10101
        if mst(S, mid):
            left = mid + 1
        else:
            right = mid - 1


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(M)]

left = 10 * 8
right = -1
for _, __, w in G:
    left = min(left, w)
    right = max(left, w)

L = binary_search(left, right)

FS = [-1] * 10101
print(L)
mst(FS, L)
print(FS[1 : N + 1])
