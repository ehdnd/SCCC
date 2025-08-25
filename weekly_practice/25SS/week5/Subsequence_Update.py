import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    T = II()
    for _ in range(T):
        N, L, R = MIS()
        A = [*MIS()]
        print(
            min(sum(sorted(A[:R])[: R - L + 1]), sum(sorted(A[L - 1 :])[: R - L + 1]))
        )

    return


if __name__ == "__main__":
    solve()
