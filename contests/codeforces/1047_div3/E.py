import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N, K = MIS()
        A = [*MIS()]
        A.sort()
        p = -1
        for i in range(len(A)):
            if A[i] != i:
                p = i
                break
        if p < 0:
            print(N * (N - 1) // 2)
            continue

        def f(arr):
            B = sorted(list(set(arr)))
            mex = len(B)
            for i in range(len(B)):
                if B[i] != i:
                    mex = i
                    break

            cnts = defaultdict(int)
            for a in arr:
                cnts[a] += 1

            a1 = []
            for x in arr:
                if x < mex and cnts[x] == 1:
                    a1.append(x)
                else:
                    a1.append(mex)
            a1.sort()
            return a1

        a1 = f(A)
        if K == 1:
            print(sum(a1))
            continue

        a2 = f(a1)
        if not K & 1:
            print(sum(a2))
        else:
            a3 = f(a2)
            print(sum(a3))

    return


if __name__ == "__main__":
    solve()
