import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    zarisu = [0, 9]
    zarisu_hap = [0, 55]
    for i in range(2, 15):
        zarisu.append(i * 9 * 10 ** (i - 1))
        zarisu_hap.append(45 * (10 ** (i - 1) + (i - 1) * 9 * 10 ** (i - 2)))

    print(zarisu)
    print(zarisu_hap)

    memo = [[0] * 15 for _ in range(10)]

    T = II()
    for t in range(T):
        N = II()
        ans = 0
        for zari in range(15):
            if N < zarisu[zari]:
                break
            N -= zarisu[zari]

        print(zari, N)

        ans += sum(zarisu_hap[:zari])

    return


if __name__ == "__main__":
    solve()
