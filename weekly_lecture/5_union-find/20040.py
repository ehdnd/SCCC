import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
MAX = 1010101


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
    cnt = 0
    isC = False
    for i in range(M):
        a, b = MIS()
        cnt += 1
        if not Union(a, b):
            isC = True
            break

    print(cnt if isC else 0)
    return


if __name__ == "__main__":
    S = [-1] * MAX
    solve()
