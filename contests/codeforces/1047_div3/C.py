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
        # 홀 홀
        if a & 1 and b & 1:
            print(a * b + 1)
        elif (a * b) % 4:
            print(-1)
        elif not a & 1 and b & 1:
            print(-1)
        else:
            print(a * b // 2 + 2)

    return


if __name__ == "__main__":
    solve()
