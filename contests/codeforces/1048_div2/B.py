import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N, M = MIS()
        A = sorted([*MIS()], reverse=True)

        ps = [0] * (N + 1)
        for i in range(N):
            ps[i + 1] = ps[i] + A[i]

        ans = 0
        for i in range(1, min(N, M) + 1):
            ans += ps[i]

        if M > N:
            ans += (M - N) * ps[N]

        print(ans)

    return


if __name__ == "__main__":
    solve()
