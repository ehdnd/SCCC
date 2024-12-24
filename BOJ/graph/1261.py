import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def chk(i: int, K: int):
    return 0 <= i <= K


def bfs(a: int, b: int):
    q = deque()
    q.append([a, b])
    L[a][b] = 0
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            return L[x][y]

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if chk(nx, N - 1) and chk(ny, M - 1):
                lv_diff = G[nx][ny]
                if L[nx][ny] > L[x][y] + lv_diff:
                    L[nx][ny] = L[x][y] + lv_diff
                    if lv_diff == 1:
                        q.append([nx, ny])
                    else:
                        q.appendleft([nx, ny])

    return


def solve() -> None:
    print(bfs(0, 0))
    return


if __name__ == "__main__":
    M, N = MIS()
    G = [list(map(int, input())) for _ in range(N)]
    L = [[INF] * M for _ in range(N)]
    solve()
