import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()


def Find(S, a):
    if S[a] < 0:
        return a
    S[a] = Find(S, S[a])
    return S[a]


def Union(S, a, b):
    a = Find(S, a)
    b = Find(S, b)
    if a == b:
        return 0
    S[a] += S[b]
    S[b] = a
    return 1


def mst(Temp, G):
    d = dict(zip(["A", "B", "C", "D", "E"], Temp))
    G.sort(key=lambda x: d[x[-1]])
    S = [-1] * (N + 1)
    res = dict.fromkeys(["A", "B", "C", "D", "E"], 0)
    for a, b, w in G:
        if Union(S, int(a), int(b)):
            res[w] += 1
        if -S[Find(S, int(a))] == N:
            break
    return res


def generate_cases(G):
    Cases = {}
    for Temp in permutations([1, 2, 3, 4, 5]):  # 1~5 중복 순열
        case = mst(Temp, G)
        Cases["".join(map(str, Temp))] = case
    return Cases


N, M, Q = map(int, input().split())
G = [list(input().split()) for _ in range(M)]

Cases = generate_cases(G)

for _ in range(Q):
    query = list(map(int, input().split()))
    asdf = list(zip([1, 2, 3, 4, 5], query))
    asdf.sort(key=lambda x: x[-1])
    tttt = list(enumerate(asdf))
    tttt.sort(key=lambda x: x[1][0])
    final = ""
    for i in range(5):
        final += str(tttt[i][0] + 1)

    final_case = Cases[final]

    res = 0
    school = ["A", "B", "C", "D", "E"]
    for i in range(5):
        res += query[i] * final_case[school[i]]
    print(res)
