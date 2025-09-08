import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        a, b = MIS()
        if a == b:
            print(0)
        elif not a % b or not b % a:
            print(1)
        else:
            print(2)

    return


if __name__ == "__main__":
    solve()
