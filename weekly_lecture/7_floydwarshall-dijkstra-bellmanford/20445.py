import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e18)


def solve() -> None:
    N, Q = MIS()
    Lines = []
    S = set()
    for _ in range(N):
        st, ed = MIS()
        Lines.append((st, ed))
        S.add(st)
        S.add(ed)
    S = sorted(list(S))

    len_S = len(S)
    dist = [[INF] * len_S for _ in range(len_S)]
    for i in range(len_S):
        dist[i][i] = 0

    for st, ed in Lines:
        st_m = bisect_left(S, st)
        ed_m = bisect_left(S, ed)
        dist[st_m][ed_m] = ed - st + 1

    for i in range(len_S - 1):
        ed, st = i, i + 1
        dist[st][ed] = 0

    for x in range(len_S):
        for st in range(len_S):
            for ed in range(len_S):
                dist[st][ed] = min(dist[st][ed], dist[st][x] + dist[x][ed])

    for _ in range(Q):
        st, ed = MIS()
        if st < S[0] or S[-1] < ed:
            print(-1)
            continue
        st_m = bisect_left(S, st)
        ed_m = bisect_left(S, ed)
        if st not in S:
            st_m -= 1
        if dist[st_m][ed_m] == INF:
            print(-1)
            continue
        print(dist[st_m][ed_m])

    return


if __name__ == "__main__":
    solve()
