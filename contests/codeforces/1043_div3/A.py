import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        A = II()
        a = input()
        B = II()
        b = input()
        c = input()

        aa = ""
        bb = ""
        for i in range(B):
            if c[i] == "D":
                aa += b[i]
            else:
                bb += b[i]

        print(bb[::-1] + a + aa)

    return


if __name__ == "__main__":
    solve()
