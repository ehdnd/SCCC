import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(I, K, T):
    q = deque()
    q.append(K)
    visit[K[0]][K[1]] = 1
    dx, dy = [2, 2, 1, 1, -2, -2, -1, -1], [1, -1, 2, -2, 1, -1, 2, -2]

    while q:
        x, y = q.popleft()
        if T == [x, y]:
            return visit[x][y]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > I - 1 or ny < 0 or ny > I - 1 or visit[nx][ny]:
                continue
            q.append([nx, ny])
            visit[nx][ny] = visit[x][y] + 1
    return 0


N = int(input())
for _ in range(N):
    I = int(input())
    K = list(map(int, input().split()))
    T = list(map(int, input().split()))
    G = [[0] * I for _ in range(I)]
    visit = [[0] * I for _ in range(I)]
    print(BFS(I, K, T) - 1)
