import sys

input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())


def solve() -> None:
    N = II()
    A = input().split()
    O = input().strip()

    if N == 1:
        print(0 if A[0] == O else 1)
        return

    want = O == "T"
    M_isTrue = A[-1] == "T"
    M_isAnd = A[-2] == "&"

    L_isTrue = A[0] == "T"
    isAnd = None
    for i in range(N - 1):
        if i & 1:
            isAnd = A[i] == "&"
        else:
            if isAnd:
                L_isTrue = L_isTrue and (A[i] == "T")
            else:
                L_isTrue = L_isTrue or (A[i] == "T")

    if not M_isAnd:
        if M_isTrue:
            if L_isTrue:
                print(0 if want else 2)
            else:
                print(0 if want else 1)
        else:
            if L_isTrue:
                print(0 if want else 1)
            else:
                print(1 if want else 0)
    else:
        if M_isTrue:
            if L_isTrue:
                print(0 if want else 1)
            else:
                print(1 if want else 0)
        else:
            if L_isTrue:
                print(1 if want else 0)
            else:
                print(2 if want else 0)


if __name__ == "__main__":
    solve()
