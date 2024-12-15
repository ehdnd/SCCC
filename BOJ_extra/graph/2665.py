import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def bfs():
    q = deque()
    q.append([0, 0])
    V[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == y == N - 1:
            return V[x][y]
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            l = not G[nx][ny]
            if V[nx][ny] <= V[x][y] + l:
                continue
            V[nx][ny] = V[x][y] + l
            q.appendleft([nx, ny]) if l == 0 else q.append([nx, ny])

    return


def solve() -> None:
    print(bfs())
    return


if __name__ == "__main__":
    N = II()
    G = [list(map(int, input())) for _ in range(N)]
    V = [[INF] * N for _ in range(N)]
    solve()
