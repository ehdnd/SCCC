import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    A = [*MIS()]
    B = [0] * N

    p = 0
    for i in range(N):
        if p >= A[i]:
            B[i] = A[i]
        else:
            B[i] = p + 1
        p = B[i]

    print(max(B))
    return


if __name__ == "__main__":
    solve()
