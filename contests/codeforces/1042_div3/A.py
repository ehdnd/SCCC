import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    T = II()
    for t in range(T):
        N = II()
        A = [*MIS()]
        B = [*MIS()]

        ans = 0
        for i in range(N):
            if A[i] > B[i]:
                ans += A[i] - B[i]
        print(ans + 1)

    return


if __name__ == "__main__":
    solve()
