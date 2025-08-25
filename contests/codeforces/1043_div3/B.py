import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N = input()
        l = len(N)
        N = int(N)

        ans = []
        for i in range(1, l):
            k = 10**i + 1
            if N % k == 0:
                ans.append(N // k)

        if ans:
            print(len(ans))
            ans.reverse()
            print(*ans)
        else:
            print(0)

    return


if __name__ == "__main__":
    solve()
