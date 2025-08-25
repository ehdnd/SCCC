import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    T = II()
    # 미리 전처리
    w_cnts = [1]
    w_prcs = [3]
    for i in range(1, 20):
        w_cnts.append(3**i)
        w_prcs.append(w_prcs[-1] * 3 + 3 ** (i - 1))

    for t in range(T):
        N, K = MIS()
        ans = 0
        sel = [0] * 20

        for i in range(19, -1, -1):
            if N == 0:
                break
            c = N // w_cnts[i]

            if c:
                ans += c * w_prcs[i]
                N -= c * w_cnts[i]
                sel[i] += c

        dd = K - sum(sel)
        if dd < 0:
            print(-1)
            continue

        dd //= 2

        for i in range(19, 0, -1):
            if dd == 0:
                break

            if sel[i] <= dd:
                dd -= sel[i]
                sel[i - 1] += 3 * sel[i]
                ans -= (3 ** (i - 1)) * sel[i]
                sel[i] = 0
            else:
                sel[i - 1] += 3 * dd
                ans -= (3 ** (i - 1)) * dd
                sel[i] -= dd
                dd = 0

        print(ans)

    return


if __name__ == "__main__":
    solve()
