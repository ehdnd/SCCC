import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve(tt: int) -> None:
    N = II()
    A = [*MIS()]
    C = [0] * 101
    for a in A:
        C[a] += 1
    maxi = 0
    for i in range(1, 100):
        cnt = 0
        for c in C:
            if c >= i:
                cnt += i
        maxi = max(cnt, maxi)
    print(maxi)
    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
