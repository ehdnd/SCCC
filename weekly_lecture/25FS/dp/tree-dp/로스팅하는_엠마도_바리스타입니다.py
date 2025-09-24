import sys

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve(tt: int) -> None:
    N = II()
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, w = MIS()
        a -= 1
        b -= 1
        adj[a].append((b, w))
        adj[b].append((a, w))

    # 루트 0
    # sz[i] i를 루트로 하는 서브트리의 노드 개수
    sz = [0] * N
    # dp1[i] i를 루트로 하는 서브트리의 이동 거리 총합 - 안
    dp1 = [0] * N
    # dp2[i] i의 부모로 가는 (반대방향) 거리 총합 - 바깥
    dp2 = [0] * N
    # dp2[0] = dp1[0]

    def dfs1(c: int, p: int) -> None:
        sz[c] = 1
        for u, w in adj[c]:
            if u != p:
                dfs1(u, c)
                dp1[c] += dp1[u] + w * sz[u]
                sz[c] += sz[u]

    def dfs2(c: int, p: int) -> None:
        for u, w in adj[c]:
            if u != p:
                # dp1[c] + dp2[c]: c를 기준으로한 거리 총합
                dp2[u] = (dp1[c] + dp2[c]) - (dp1[u] + sz[u] * w) + w * (N - sz[u])
                dfs2(u, c)

    dfs1(0, -1)
    dfs2(0, -1)

    for i in range(N):
        print(dp1[i] + dp2[i])

    return


if __name__ == "__main__":
    T = 1
    for tt in range(T):
        solve(tt)
