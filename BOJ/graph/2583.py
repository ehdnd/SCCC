import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def paint_graph() -> None:
    n1, m1, n2, m2 = MIS()
    for m in range(m1, m2):
        for n in range(n1, n2):
            G[m][n] = 1
    return


def bfs(m: int, n: int, area: int) -> None:
    q = deque()
    q.append([m, n])
    V[m][n] = area
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1 or V[nx][ny] or G[nx][ny]:
                continue
            V[nx][ny] = area
            q.append([nx, ny])

    return


def find_area() -> int:
    area = 0
    for m in range(M):
        for n in range(N):
            if V[m][n] or G[m][n]:
                continue
            area += 1
            bfs(m, n, area)
    return area


def solve() -> None:
    for _ in range(K):
        paint_graph()

    area = find_area()

    temp = [0] * 10101
    for m in range(M):
        for n in range(N):
            if not V[m][n]:
                continue
            temp[V[m][n]] += 1

    res = []
    for x in temp:
        if x == 0:
            continue
        res.append(x)
    res.sort()

    print(area)
    print(*res)

    return


if __name__ == "__main__":
    M, N, K = MIS()
    G = [[0] * N for _ in range(M)]
    V = [[0] * N for _ in range(M)]
    solve()
