import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


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


def solve() -> None:
    N, M = MIS()
    Schools = list(input().split())
    Edges = []
    for _ in range(M):
        a, b, r = MIS()
        if Schools[a - 1] == Schools[b - 1]:
            continue
        Edges.append([r, a, b])
    Edges.sort()

    res = 0
    for r, a, b in Edges:
        if Union(a, b):
            res += r
        if -S[Find(a)] == N:
            print(res)
            return
    print(-1)
    return


if __name__ == "__main__":
    S = [-1] * 1010
    solve()
