import sys
from itertools import permutations

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


N, M, Q = map(int, input().split())
G = [[] for _ in range(5)]
School = [0, 1, 2, 3, 4]
Cases = {}

# 가중치별로 간선을 저장하자
for _ in range(M):
    a, b, w = input().split()
    w = ord(w) - ord("A")
    G[w].append([int(a), int(b)])

for case in permutations(School):
    S = [-1] * (N + 1)
    res = [0] * 5
    for i in case:
        isMade = False
        for u, v in G[i]:
            if Union(u, v):
                res[i] += 1
            if -S[Find(u)] == N:
                isMade = True
                break
        if isMade:
            break
    Cases[case] = res

for _ in range(Q):
    query = list(map(int, input().split()))
    q = list(zip(query, School))
    q.sort()
    query_key = tuple([q[i][1] for i in range(5)])
    final_case = Cases[query_key]

    res = 0
    for i in range(5):
        res += query[i] * final_case[School[i]]
    print(res)
