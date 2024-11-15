import sys

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
        return False
    if S[a] > S[b]:
        a, b = b, a
    S[a] += S[b]
    S[b] = a
    return True


def jud():
    N, K = int(input()), int(input())
    S = [-1] * 101010
    for _ in range(K):
        a, b = map(int, input().split())
        Union(S, a, b)
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(1) if Find(S, a) == Find(S, b) else print(0)

    return


T = int(input())
for i in range(T):
    print(f"Scenario {i+1}:")
    jud()
    print()
