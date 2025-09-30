import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e18)


def solve(tt: int) -> None:
    N = II()
    A = [*MIS()]
    st = 0
    for i in range(N):
        if (i + 1) & 1:
            st += A[i]
        else:
            st -= A[i]

    ans = st

    if N >= 3:
        o_idx = N if N & 1 else N - 1
        cost = o_idx - 1
        ans = max(ans, st + cost)

    if N >= 4:
        e_idx = N if not N & 1 else N - 1
        cost = e_idx - 2
        ans = max(ans, st + cost)

    if N >= 2:
        pluso = INF
        for r in range(1, N + 1):
            if not r & 1:
                if pluso != INF:
                    tmp = st + (r + 2 * A[r - 1]) - pluso
                    ans = max(ans, tmp)
            else:
                pluso = min(pluso, r + 2 * A[r - 1])

        minuse = INF
        for r in range(1, N + 1):
            if r & 1:
                if minuse != INF:
                    tmp = st + (r - 2 * A[r - 1]) - minuse
                    ans = max(ans, tmp)
            else:
                minuse = min(minuse, r - 2 * A[r - 1])

    print(ans)

    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
