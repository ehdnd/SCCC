import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())
MAX = 500000


def bfs(st: int) -> list:
    V = [[-1, -1] for _ in range(MAX + 1)]
    q = deque()
    q.append([st, 0])
    V[st][0] = 0
    while q:
        x, e = q.popleft()
        for nx in [x - 1, x + 1, 2 * x]:
            ne = 1 - e
            if nx < 0 or nx > MAX or V[nx][ne] >= 0:
                continue
            V[nx][ne] = V[x][e] + 1
            q.append([nx, ne])

    return V


def find_K(K: int, V: list) -> int:
    t, e = 0, 0
    while 1:
        x = K + (t * (t + 1) // 2)
        if x > MAX:
            break
        N_t = V[x][e]
        if N_t != -1 and N_t <= t:
            return t
        e = 1 - e
        t += 1
    return -1


def solve() -> None:
    N, K = MIS()
    V = bfs(N)
    print(find_K(K, V))
    return


if __name__ == "__main__":
    solve()
