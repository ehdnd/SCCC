import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    for t in range(T):
        N, K = MIS()
        A = [*MIS()]
        B = [*MIS()]

        AA = [min(x % K, (K - x % K) % K) for x in A]
        BB = [min(x % K, (K - x % K) % K) for x in B]

        print("YES" if AA == BB else "NO")

    return


if __name__ == "__main__":
    solve()
