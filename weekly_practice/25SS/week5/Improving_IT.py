import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e18)


def solve() -> None:
    N, M = MIS()
    A = [[0]] + [[*MIS()] for _ in range(N)]
    dp = [0, 0]

    for i in range(2, N + 2):
        dp.append(INF)
        for j in range(max(1, i - M), i):
            dp[i] = min(dp[i], dp[j] + A[j][0] - A[j][i - j])

    print(dp[N + 1])
    return


if __name__ == "__main__":
    solve()
