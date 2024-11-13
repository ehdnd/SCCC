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


N, M, Q = map(int, input().split())
Conn = [list(map(int, input().split())) for _ in range(M)]
Query = []
Bool = [0] * M
S = [-1] * 101010

for _ in range(Q):
    query = int(input()) - 1
    Bool[query] = 1
    Query.append(query)

for i in range(M):
    if not Bool[i]:
        a, b = Conn[i]
        Union(a, b)

Query = Query[::-1]
res = 0
for query in Query:
    a, b = Conn[query]
    a, b = Find(a), Find(b)
    if a != b:
        res += S[a] * S[b]
    Union(a, b)

print(res)
