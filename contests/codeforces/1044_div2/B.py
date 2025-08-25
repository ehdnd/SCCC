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
        A = [*MIS()]
        A.sort(key=lambda x: -x)
        ans = 0
        for i in range(0, len(A), 2):
            ans += A[i]
        print(ans)

    return


if __name__ == "__main__":
    solve()
