import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N, M = MIS()
    s = [*input()]
    ss = sorted(list(enumerate(s)), key=lambda x: x[1])
    ss = ss[M:]
    ss.sort(key=lambda x: x[0])
    print("".join(map(lambda x: x[1], ss)))
    return


if __name__ == "__main__":
    solve()
