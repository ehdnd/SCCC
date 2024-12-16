import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def find_max(G: list, dp: list, n: int) -> list:
    for e in range(2):
        if n == 1:
            dp[e][n] = G[e][n]
        elif n == 2:
            dp[e][n] = G[1 - e][n - 1] + G[e][n]
        else:
            dp[e][n] = max(dp[1 - e][n - 2], dp[1 - e][n - 1]) + G[e][n]
    return dp


def solve() -> None:
    N = II()
    G = [[0] + list(MIS()) for _ in range(2)]
    dp = [[0] * (N + 1) for _ in range(2)]

    for n in range(1, N + 1):
        dp = find_max(G, dp, n)

    print(max(dp[0][N], dp[1][N]))
    return


if __name__ == "__main__":
    T = II()
    for _ in range(T):
        solve()
