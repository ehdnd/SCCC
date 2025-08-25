import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N = II()
        for i in range(N):
            if not N & 1 and i == N - 1:
                print(2, end=" ")
                break

            if i & 1:
                print(3, end=" ")
            else:
                print(-1, end=" ")
        print()

    return


if __name__ == "__main__":
    solve()
