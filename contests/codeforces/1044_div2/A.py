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
        A = set([*MIS()])
        if len(A) == N:
            print("NO")
        else:
            print("YES")

    return


if __name__ == "__main__":
    solve()
