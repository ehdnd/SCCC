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
# 인접리스트로 그래프 저장
edge = [[] for _ in range(5)]
for u, v, w in G:
    edge[ord(w) - 65].append((int(u), int(v)))
School = [0, 1, 2, 3, 4]

Res_cases = {}

# [0, 1, 2, 3, 4] 을 노드로 하는 간선이 존재 / 인접 리스트로 그래프
# [permutation 으로 가능한 조합 추출] = [1, 0 ,2, 4, 3]
# 조합 추출이 결국 가중치로 sort 하는 것과 동일
# edge 에 접근해서 간선을 찾는다는 것 자체가 이미 MST 조건 충족

# MST 구성에 사용된 간선 수 저장하자
for case in permutations(School):
    S = [-1] * (N + 1)
    res = [0] * 5
    print(case)
    for i in case:
        print(i)
        op = 1
        for u, v in edge[i]:
            if Union(u, v):
                res[i] += 1
            if -S[Find(u)] == N:
                op = 0
                break
        if op == 0:
            break
    print(res)
    Res_cases[case] = res

# 쿼리 깎는건 그대로..
for _ in range(Q):
    query = list(map(int, input().split()))
    q = list(zip(query, School))
    q.sort()
    query_key = tuple([q[i][1] for i in range(5)])
    final_case = Res_cases[query_key]

    res = 0
    for i in range(5):
        res += query[i] * final_case[School[i]]
    print(res)
