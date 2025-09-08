import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N = II()
        A = [*MIS()]
        for a in A:
            print(N - a + 1, end=" ")
        print()

    return


if __name__ == "__main__":
    solve()
