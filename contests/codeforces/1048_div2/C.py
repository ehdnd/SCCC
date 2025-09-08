import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    T = II()
    for t in range(T):
        K, X = MIS()
        ans = []
        while 1:
            if X == (1 << K):
                break
            if X > (1 << K):
                ans.append(2)
                X = 2 * (X - (1 << K))
            else:
                ans.append(1)
                X <<= 1

        print(len(ans))
        print(*ans[::-1])

    return


if __name__ == "__main__":
    solve()
