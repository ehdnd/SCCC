def Make(i):
    if i == 0:
        return "-"
    s = Make(i - 1) + " " * (3 ** (i - 1)) + Make(i - 1)
    return s


def solve() -> None:
    print(Make(N))
    return


if __name__ == "__main__":
    while 1:
        try:
            N = int(input())
            solve()
        except EOFError:
            break
