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
        # 모노톤 - L / R
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
        # i 시작 중간 md, 끝 ed
        # ===========================

        st = [[] for _ in range(N)]
        for i in range(N):
            if L[i] != -1 and R[i] != N:
                st[L[i]].append((i, R[i]))

        # ===========================
        # 오프라인 쿼리
        # ===========================

        qs = []
        for i in range(Q):
            l, r = MIS()
            qs.append((l - 1, r - 1, i))
        qs.sort(reverse=True)

        # ===========================
        # q(a, b) -> 중간점 md 가 a, b 사이에 있는 최소 끝점 ed 관리
        # ===========================

        sz = 1
        while sz < N:
            sz <<= 1
        seg = [N] * (sz << 1)

        q_idx = 0
        ans = [""] * Q

        # ===========================
        # i 시작 스위핑 라인
        # ===========================

        for i in range(N - 1, -1, -1):
            for md, ed in st[i]:
                k = md + sz
                seg[k] = min(seg[k], ed)
                while k > 1:
                    k >>= 1
                    seg[k] = min(seg[k * 2], seg[k * 2 + 1])

            # ===========================
            # [i, r] 쿼리 - 가장 빨리 끝나는 ed
            # ===========================

            while q_idx < Q and qs[q_idx][0] == i:
                l, r, o_idx = qs[q_idx]

                res = N
                ll = l + sz
                rr = r + sz + 1

                while ll < rr:
                    if ll & 1:
                        res = min(res, seg[ll])
                        ll += 1
                    if rr & 1:
                        rr -= 1
                        res = min(res, seg[rr])
                    ll >>= 1
                    rr >>= 1

                ans[o_idx] = "NO" if res <= r else "YES"
                q_idx += 1

        # ===========================

        print(*ans, sep="\n")

    return


if __name__ == "__main__":
    solve()
