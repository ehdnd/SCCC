import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    A = 1000 - II()
    ans = 0
    B = [500, 100, 50, 10, 5, 1]
    for b in B:
        ans += A // b
        A %= b
    print(ans)
    return


if __name__ == "__main__":
    solve()
