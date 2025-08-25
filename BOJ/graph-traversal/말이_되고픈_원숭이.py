import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def in_range(r: int, c: int, N: int, M: int):
    return 0 <= r < N and 0 <= c < M


def solve() -> None:
    K = II()
    M, N = MIS()
    B = [[*MIS()] for _ in range(N)]
    vis = [[[0] * (K + 1) for _ in range(M)] for __ in range(N)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    drh = [2, 2, -2, -2, 1, 1, -1, -1]
    dch = [1, -1, 1, -1, 2, -2, 2, -2]

    vis[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0))

    while q:
        r, c, k = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not in_range(nr, nc, N, M) or vis[nr][nc][k] or B[nr][nc]:
                continue

            vis[nr][nc][k] = vis[r][c][k] + 1
            q.append((nr, nc, k))

        for i in range(8):
            nr = r + drh[i]
            nc = c + dch[i]

            if not in_range(nr, nc, N, M) or k >= K or vis[nr][nc][k + 1] or B[nr][nc]:
                continue

            vis[nr][nc][k + 1] = vis[r][c][k] + 1
            q.append((nr, nc, k + 1))

    ans = INF
    for x in vis[N - 1][M - 1]:
        if x:
            ans = min(x - 1, ans)

    print(ans if ans != INF else -1)

    return


if __name__ == "__main__":
    solve()
