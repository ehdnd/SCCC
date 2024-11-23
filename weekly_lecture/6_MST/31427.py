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
        return 0
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return 1


N, M, Q = map(int, input().split())
G = [list(input().split()) for _ in range(M)]
School = ["A", "B", "C", "D", "E"]

Cases = [c for c in permutations(["A", "B", "C", "D", "E"])]
Res_cases = {}

for case in Cases:
    school_to_w = dict(zip(case, [1, 2, 3, 4, 5]))

    G.sort(key=lambda x: school_to_w[x[-1]])
    S = [-1] * (N + 1)
    res = dict(zip(School, [0, 0, 0, 0, 0]))
    for a, b, w in G:
        if Union(int(a), int(b)):
            res[w] += 1
        if -S[Find(int(a))] == N:
            break

    Res_cases[case] = res

for _ in range(Q):
    query = list(map(int, input().split()))
    q = list(zip(query, School))
    q.sort()
    query_key = tuple([q[i][1] for i in range(5)])
    final_case = Res_cases[query_key]

    res = 0
    school = ["A", "B", "C", "D", "E"]
    for i in range(5):
        res += query[i] * final_case[school[i]]
    print(res)

# [2, 3, 5, 4, 1] 은 [2인 B의 가중치가 인덱스만큼이라는 뜻]
# [1, 2, 3, 5, 4] Cases 중 하나..
