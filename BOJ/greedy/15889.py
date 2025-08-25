import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    A = [*MIS()]
    B = [*MIS()]
    poss = 0
    for i in range(N - 1):
        if A[i] <= poss:
            poss = max(poss, A[i] + B[i])
        else:
            print("엄마 나 전역 늦어질 것 같아")
            return
    if A[-1] <= poss:
        print("권병장님, 중대장님이 찾으십니다")
    else:
        print("엄마 나 전역 늦어질 것 같아")

    return


if __name__ == "__main__":
    solve()
