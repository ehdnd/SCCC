import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def bfs() -> None:
    q = deque()
    m, n, wall_break = 0, 0, 0
    q.append([m, n, wall_break])
    V[0][0][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        x, y, wall_break = q.popleft()
        if x == N - 1 and y == M - 1:
            return V[N - 1][M - 1][wall_break]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1 or V[nx][ny][wall_break]:
                continue
            next_wall_break = wall_break
            # 다음이 벽이다
            if G[nx][ny]:
                if wall_break == K:
                    continue
                next_wall_break = wall_break + 1
                if V[nx][ny][next_wall_break]:
                    continue
            V[nx][ny][next_wall_break] = V[x][y][wall_break] + 1
            q.append([nx, ny, next_wall_break])

    return -1


def solve() -> None:
    res = bfs()
    print(res)
    return


if __name__ == "__main__":
    N, M, K = MIS()
    G = [list(map(int, input())) for _ in range(N)]
    V = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    solve()
