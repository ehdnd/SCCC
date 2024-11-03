import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(N, M, G, visit):
    q = deque()
    q.append([0, 0, 0])
    visit[0][0][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y, wall_break = q.popleft()
        if x == N - 1 and y == M - 1:
            return visit[x][y][wall_break]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            # 다음칸이 이동가능
            if G[nx][ny] == 0 and not visit[nx][ny][wall_break]:
                q.append([nx, ny, wall_break])
                visit[nx][ny][wall_break] = visit[x][y][wall_break] + 1
            # 다음칸이 벽
            elif G[nx][ny] == 1 and not wall_break:
                q.append([nx, ny, 1])
                visit[nx][ny][1] = visit[x][y][0] + 1

    return -1


N, M = map(int, input().split())
G = [list(map(int, input())) for _ in range(N)]
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
print(BFS(N, M, G, visit))

# for i in range(N):
#     for j in range(M):
#         print(visit[i][j][0], end=" ")
#     print()

# for i in range(N):
#     for j in range(M):
#         print(visit[i][j][1], end=" ")
#     print()
