import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


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
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue

            l = G[nx][ny]
            if L[nx][ny] <= L[x][y] + l:
                continue
            L[nx][ny] = L[x][y] + l
            q.appendleft([nx, ny]) if l == 0 else q.append([nx, ny])

    return


def solve() -> None:
    print(bfs(0, 0))
    return


if __name__ == "__main__":
    M, N = MIS()
    G = [list(map(int, input())) for _ in range(N)]
    L = [[INF] * M for _ in range(N)]
    solve()
