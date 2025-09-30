import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)

# 전체를 몽땅 합치고 각각을 뺏을 때 가능한지 확인
# 가능한게 2개 이상이면 가능 -> TLE

#


def solve(tt: int) -> None:
    N, M = MIS()
    A = [[*MIS()][1:] for _ in range(N)]
    C = [0] * (M + 1)
    for s in A:
        for x in s:
            C[x] += 1

    for s in A:
        CC = list(C)
        for x in s:
            CC[x] -= 1
        for i in range(1, M + 1):
            if not CC[i]:
                break
        else:
            print("YES")
            return

    print("NO")

    return


if __name__ == "__main__":
    T = 1
    T = II()
    for tt in range(T):
        solve(tt)
