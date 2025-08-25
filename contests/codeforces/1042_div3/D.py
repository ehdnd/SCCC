import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    T = II()
    for t in range(T):
        N = II()
        if N == 2:
            input()
            print(0)
            continue

        adj = [[] for _ in range(N)]
        for _ in range(N - 1):
            a, b = MIS()
            a -= 1
            b -= 1
            adj[a].append(b)
            adj[b].append(a)

        ans = 0
        for i in range(N):
            if len(adj[i]) == 1:
                ans += 1

        mx = 0
        for i in range(N):
            cnt = 0
            for x in adj[i]:
                cnt += len(adj[x]) == 1
            mx = max(mx, cnt)

        print(ans - mx)
    return


if __name__ == "__main__":
    solve()
