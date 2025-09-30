import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve(tt: int) -> None:
    N = II()
    A = [[*MIS()] for _ in range(N)]
    A.sort(key=lambda x: -(x[0] + x[1]))

    ans = 0
    for l, r in A:
        ans += r - l

    i = 0
    while 1:
        if i == N // 2:
            break
        ans += A[i][1]
        i += 1

    i = 0
    while 1:
        if i == N // 2:
            break
        ans -= A[N - i - 1][0]
        i += 1

    print(ans)

    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
