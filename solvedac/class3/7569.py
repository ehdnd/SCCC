import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs():
    q = deque(S)
    while q:
        h, n, m = q.popleft()
        dh, dn, dm = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
        for i in range(6):
            nh, nn, nm = h + dh[i], n + dn[i], m + dm[i]
            if (
                nh < 0
                or nh > H - 1
                or nn < 0
                or nn > N - 1
                or nm < 0
                or nm > M - 1
                or G[nh][nn][nm]
            ):
                continue
            q.append([nh, nn, nm])
            G[nh][nn][nm] = G[h][n][m] + 1

    res = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                cur = G[h][n][m]
                if cur == 0:
                    return -1
                res = max(res, cur)
    return res - 1


M, N, H = map(int, input().split())
G = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
S = []
for h in range(H):
    for n in range(N):
        for m in range(M):
            if G[h][n][m] == 1:
                S.append([h, n, m])

print(bfs())
