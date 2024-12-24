import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    G = [list(MIS()) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    dp[N - 1] = [G[N - 1][i] for i in range(N)]

    for i in range(N - 2, -1, -1):
        for k in range(0, i + 1):
            dp[i][k] = max(dp[i + 1][k], dp[i + 1][k + 1]) + G[i][k]

    print(dp[0][0])
    return


if __name__ == "__main__":
    solve()
