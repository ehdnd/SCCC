import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    N, M = MIS()
    A = [[*MIS()] for _ in range(N)]
    ans = 0
    for a in A:
        gamso = 0
        zunga = 0
        if a[0] > a[1]:
            gamso = 1
        elif a[0] < a[1]:
            zunga = 1
        else:
            continue

        for i in range(1, M):
            if gamso:
                if 1 <= a[i - 1] - a[i] <= 3:
                    continue
                else:
                    break
            else:
                if 1 <= a[i] - a[i - 1] <= 3:
                    continue
                else:
                    break
        else:
            ans += 1
    print(ans)

    return


if __name__ == "__main__":
    solve()
