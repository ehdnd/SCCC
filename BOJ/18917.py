import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: int(input())


def do_query(query: list, total: int, xor: int) -> tuple[int, int]:
    q, x = query[0], query[-1]
    if q < 3:
        xor ^= x
    if q == 1:
        total += x
    elif q == 2:
        total -= x
    elif q == 3:
        print(total)
    else:
        print(xor)
    return (total, xor)


def solve() -> None:
    res_total = 0
    res_xor = 0
    M = II()
    for _ in range(M):
        query = list(MIS())
        res_total, res_xor = do_query(query, res_total, res_xor)

    return


if __name__ == "__main__":
    solve()
