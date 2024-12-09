import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def do_query(N: int, query: list):
    start = deque()
    final = deque([i for i in range(N, 0, -1)])
    for q in query:
        x = final.pop()
        if q == 1:
            start.appendleft(x)
        elif q == 2:
            start.insert(1, x)
        else:
            start.append(x)

    return start


def solve() -> None:
    N = II()
    query = list(MIS())[::-1]
    start = do_query(N, query)
    print(*start)
    return


if __name__ == "__main__":
    solve()
