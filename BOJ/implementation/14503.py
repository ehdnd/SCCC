import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def check(x, y, N, M) -> bool:
    return 0 <= x < N and 0 <= y < M


def next(x, y, d) -> tuple[int, int]:
    if d == 0:
        return (x - 1, y)
    if d == 1:
        return (x, y + 1)
    if d == 2:
        return (x + 1, y)
    if d == 3:
        return (x, y - 1)


def prev(x, y, d) -> tuple[int, int]:
    if d == 0:
        return (x + 1, y)
    if d == 1:
        return (x, y - 1)
    if d == 2:
        return (x - 1, y)
    if d == 3:
        return (x, y + 1)


def run(N, M, r, c, d, G, V) -> int:
    cnt = 0

    x, y = r, c
    while 1:
        if not V[x][y]:
            V[x][y] = 1
            cnt += 1

        isClean = True
        for i in range(4):
            nx, ny = next(x, y, i)
            if not G[nx][ny] and not V[nx][ny]:
                isClean = False
                break

        if isClean:
            temp_x, temp_y = prev(x, y, d)
            if G[temp_x][temp_y]:
                return cnt
            x, y = temp_x, temp_y

        else:
            d = (d + 3) % 4
            temp_x, temp_y = next(x, y, d)
            if not G[temp_x][temp_y] and not V[temp_x][temp_y]:
                x, y = temp_x, temp_y


def solve() -> None:
    N, M = MIS()
    r, c, d = MIS()
    G = [list(MIS()) for _ in range(N)]
    V = [[0] * M for _ in range(N)]

    print(run(N, M, r, c, d, G, V))

    return


if __name__ == "__main__":
    solve()
