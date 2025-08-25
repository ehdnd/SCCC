import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    G = defaultdict(list)
    for _ in range(N):
        a, b = MIS()
        G[a].append(b)
        G[b].append(a)

    vis = [0] * (N + 1)

    def dfs(c: int, p: int) -> int:
        vis[c] = vis[p] + 1
        for nx in G[c]:
            if nx == p:
                continue
            elif vis[nx]:
                return vis[c] - vis[nx] + 1
            else:
                res = dfs(nx, c)
                if res:
                    return res

        return 0

    cnt = dfs(1, 0)
    print(3 if cnt & 1 else 2)
    return


if __name__ == "__main__":
    solve()
