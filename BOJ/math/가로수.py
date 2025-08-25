import sys
import math

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N = II()
    G = [II() for _ in range(N)]
    A = []
    for i in range(1, N):
        A.append(G[i] - G[i - 1])

    b = math.gcd(*A)
    ans = 0
    for a in A:
        ans += a // b - 1
    print(ans)
    return


if __name__ == "__main__":
    solve()
