import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N, Q = MIS()
        A = [*MIS()]

        # ===========================
        # 모노톤
        # L[i] i 왼쪽 - 시작
        # R[i] i 오른쪽 - 끝
        # ===========================

        R = [N] * N
        stk = []
        for i in range(N - 1, -1, -1):
            while stk and A[stk[-1]] >= A[i]:
                stk.pop()
            if stk:
                R[i] = stk[-1]
            stk.append(i)

        L = [-1] * N
        stk = []
        for i in range(N):
            while stk and A[stk[-1]] <= A[i]:
                stk.pop()
            if stk:
                L[i] = stk[-1]
            stk.append(i)

        # ===========================
        # i 까지 가장 오른쪽 시작점
        # ===========================

        st = [-1] * N
        for i in range(N):
            if L[i] != -1 and R[i] != N:
                st[R[i]] = max(st[R[i]], L[i])

        for i in range(1, N):
            st[i] = max(st[i], st[i - 1])

        for _ in range(Q):
            l, r = MIS()
            l -= 1
            r -= 1
            print("YES" if st[r] < l else "NO")

    return


if __name__ == "__main__":
    solve()
