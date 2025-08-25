import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    G = defaultdict(list)
    for _ in range(N - 1):
        a, b = MIS()
        G[a].append(b)
        G[b].append(a)

    W = [*MIS()]
    dp = [0] * N
    vis = [0] * N

    def dfs(n, p):
        vis[n] = 1
        dp[n] = W[n]
        for nx in G[n]:
            if vis[nx]:
                continue
            dfs(nx, n)
            dp[n] += max(0, dp[nx])

    dfs(0, -1)

    print(dp[0])

    return


if __name__ == "__main__":
    solve()
