import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(N, M, G, V):
    temp = []
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            if G[i][j] == "F":
                temp.append([i, j, 0])
                V[i][j][0] = 1
            elif G[i][j] == "J":
                temp.append([i, j, 1])
                V[i][j][1] = 1
    q = deque(sorted(temp, key=lambda x: x[2]))

    while q:
        x, y, w = q.popleft()

        if w == 0:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    nx < 0
                    or nx > N - 1
                    or ny < 0
                    or ny > M - 1
                    or V[nx][ny][w]
                    or not G[nx][ny] == "."
                ):
                    continue
                q.append([nx, ny, w])
                V[nx][ny][w] = 1

        if w == 1:
            if x == 0 or x == N - 1 or y == 0 or y == M - 1:
                return V[x][y][1]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    nx < 0
                    or nx > N - 1
                    or ny < 0
                    or ny > M - 1
                    or V[nx][ny][0]
                    or V[nx][ny][1]
                    or not G[nx][ny] == "."
                ):
                    continue
                q.append([nx, ny, w])
                V[nx][ny][w] = V[x][y][w] + 1

    return "IMPOSSIBLE"


N, M = map(int, input().split())
G = [list(input()) for _ in range(N)]
V = [[[0, 0] for _ in range(M)] for _ in range(N)]
print(BFS(N, M, G, V))

# for i in range(N):
#     for j in range(M):
#         print(V[i][j][0], end=" ")
#     print()
# print()
# for i in range(N):
#     for j in range(M):
#         print(V[i][j][1], end=" ")
#     print()
