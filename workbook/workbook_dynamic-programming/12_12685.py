import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N, M = MIS()
    P = [0] * (N + 1)
    K = [[0] * (M + 1) for _ in range(N + 1)]
    wt = [0] * (N + 1)

    for i in range(1, N + 1):
        w, p = MIS()
        P[i] = p
        wt[i] = w

    for i in range(N + 1):
        for w in range(M + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i] <= w:
                K[i][w] = max(P[i] + K[i - 1][w - wt[i]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    print(K[N][M])

    # def isIncluded() -> list[int]:
    #     i, j = N, M
    #     x = [0] * (N + 1)
    #     while i > 0 and j > 0:
    #         if K[i][j] == K[i - 1][j]:
    #             x[i] = 0
    #         else:
    #             x[i] = 1
    #             j -= wt[i]
    #         i -= 1
    #     return x[1:]

    # print(*isIncluded())

    return


if __name__ == "__main__":
    solve()
