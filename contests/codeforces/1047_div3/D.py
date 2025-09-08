import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    N = II()
    A = [*MIS()]
    idxs = defaultdict(list)
    for i in range(N):
        a = A[i]
        idxs[a].append(i)

    for i in range(1, N + 1):
        if len(idxs[i]) % i:
            print(-1)
            return

    ans = [0] * N
    val = 1
    for cnt, idx_lst in idxs.items():
        l = len(idx_lst)

        for i in range(0, l, cnt):
            for k in range(cnt):
                idx = i + k
                ans[idx_lst[idx]] = val
            val += 1
    print(*ans)

    return


if __name__ == "__main__":
    T = II()
    for t in range(T):
        solve()
