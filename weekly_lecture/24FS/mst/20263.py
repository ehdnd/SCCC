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


def find_used_lines():
    used_lines = []
    uS = [-1] * 10101
    for a, b, w in G:
        if w < L:
            continue
        if Union(uS, a, b):
            used_lines.append([a, b, w])
        if -uS[Find(uS, a)] == N:
            return used_lines


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

G.sort(key=lambda x: x[-1])

left = min(G, key=lambda x: x[-1])[-1]
right = max(G, key=lambda x: x[-1])[-1]

L = binary_search(left, right)

FS = [-1] * 10101
mst(FS, L)
Lines = find_used_lines()[::-1]

S = [-1] * 10101
res = 0
for a, b, w in Lines:
    size_a = -S[Find(S, a)]
    size_b = -S[Find(S, b)]
    res += size_a * size_b * w
    Union(S, a, b)
print(res)
