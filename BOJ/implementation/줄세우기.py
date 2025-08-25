import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def solve() -> None:
    P = II()
    for _ in range(P):
        t, *arr = MIS()
        ans = 0
        tmp = []
        for i in range(20):
            c = arr[i]
            for j in range(len(tmp)):
                if tmp[j] > c:
                    tmp.insert(j, c)
                    ans += len(tmp) - j - 1
                    break
            else:
                tmp.append(c)

        print(t, ans)

    return


if __name__ == "__main__":
    solve()
