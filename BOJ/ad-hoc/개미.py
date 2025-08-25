import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    T = II()
    for _ in range(T):
        L, N = MIS()
        ants = [II() for _ in range(N)]
        tmp = list(map(lambda x: abs(L / 2 - x), ants))
        mini = int(abs(L / 2 - min(tmp)))
        tmp = list(map(lambda x: max(x, L - x), ants))
        maxi = max(tmp)
        print(mini, maxi)
    return


if __name__ == "__main__":
    solve()
