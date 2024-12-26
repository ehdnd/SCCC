import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N, M = MIS()
    Planes = [list(MIS()) for _ in range(M)]
    print(N - 1)


if __name__ == "__main__":
    T = II()
    for _ in range(T):
        solve()
