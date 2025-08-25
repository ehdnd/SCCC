import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    G = [[*MIS()] for _ in range(N)]
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

    for i in range(1, N):
        if G[0][i] == 1:
            break
        dp[0][i][0] = 1

    for i in range(1, N):
        for j in range(1, N):
            if G[i][j] == 1:
                continue
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if G[i - 1][j] == 0 and G[i][j - 1] == 0:
                dp[i][j][1] = (
                    dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
                )

    print(sum(dp[N - 1][N - 1]))

    return


if __name__ == "__main__":
    solve()
