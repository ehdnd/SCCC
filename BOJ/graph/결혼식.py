import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    M = II()
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = MIS()
        adj[a].append(b)
        adj[b].append(a)

    q = deque()
    q.append(1)
    vis = [0] * (N + 1)
    vis[1] = 1

    cnt = 0
    for t in range(2):
        q_sz = len(q)
        for _ in range(q_sz):
            x = q.popleft()
            for nx in adj[x]:
                if not vis[nx]:
                    vis[nx] = 1
                    cnt += 1
                    q.append(nx)

    print(cnt)

    return


if __name__ == "__main__":
    solve()
