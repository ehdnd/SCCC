import sys
from collections import deque
import heapq

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
INF = int(1e9)


def solve() -> None:
    N, K = MIS()
    pq = []

    is_include = [0] * (N + 1)
    for _ in range(K):
        v, a, b = MIS()
        is_include[v] = 1
        # 시작idx, 개수, v
        heapq.heappush(pq, (a, b - a + 1, v, (a, b)))

    ans = []
    idx = 1

    for i in range(1, N + 1):
        if not is_include[i]:
            heapq.heappush(pq, (1, N, i, (1, N)))

    while pq:
        a, dif, v, (_, b) = heapq.heappop(pq)
        print(idx, pq)
        if b < idx:
            print(-1)
            return

        ans.append(v)
        is_include[v] = 1
        idx += 1

    print(*ans)
    return


if __name__ == "__main__":
    solve()
