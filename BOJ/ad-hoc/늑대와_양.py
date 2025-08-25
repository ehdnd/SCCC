import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    R, C = MIS()
    board = [list(input()) for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == "S":
                for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= nx < R and 0 <= ny < C:
                        if board[nx][ny] == "W":
                            print(0)
                            return

    print(1)
    for row in board:
        print("".join(row).replace(".", "D"))

    return


if __name__ == "__main__":
    solve()
