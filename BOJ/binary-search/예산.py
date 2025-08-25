import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def poss(x: int, A: list[int], M: int) -> bool:
    sum = 0
    for a in A:
        sum += a if a < x else x
    return sum <= M


def solve() -> None:
    N = II()
    A = sorted([*MIS()])
    M = II()

    lo = 0
    hi = A[-1]

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if poss(mid, A, M):
            lo = mid + 1
        else:
            hi = mid - 1

    print(hi)

    return


if __name__ == "__main__":
    solve()
