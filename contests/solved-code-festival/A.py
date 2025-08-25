import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    N, K = MIS()
    A = [[*MIS()] for _ in range(K)]
    A.sort(key=lambda x: ((x[2] - x[1]), x[0]))

    ans = [0] * (N + 1)
    for v, a, b in A:
        pass

    return


if __name__ == "__main__":
    solve()
