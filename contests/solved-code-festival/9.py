import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    N, M = MIS()
    edges = [[*MIS()] for _ in range(M)]
    edges.sort(key=lambda x: -x[-1])
    st, ed = MIS()
    S = [-1] * (N + 1)
    G = defaultdict(list)

    ans = 0

    def find(a: int) -> int:
        if S[a] < 0:
            return a
        S[a] = find(S[a])
        return S[a]

    def union(a: int, b: int) -> bool:
        a = find(a)
        b = find(b)
        if a == b:
            return False
        if S[a] > S[b]:
            a, b = b, a
        S[a] += S[b]
        S[b] = a
        return True

    for a, b, w in edges:
        if union(a, b):
            G[a].append((b, w))
            G[b].append((a, w))

        if find(st) == find(ed):
            ans = w
            break
    else:
        print(-1)
        return

    vis = [0] * (N + 1)
    ggg = []

    def dfs(p, c, ed):
        vis[c] = 1
        if c == ed:
            return 1

        for nc, _ in G[c]:
            if vis[nc]:
                continue
            ret = dfs(c, nc, ed)
            if ret:
                ggg.append(c)
                return 1
        return 0

    dfs(-1, st, ed)

    ggg.reverse()
    ggg.append(ed)

    print(w)
    print(*ggg)
    return


if __name__ == "__main__":
    solve()
