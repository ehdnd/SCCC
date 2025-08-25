import sys

input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: map(int, input().split())
II = lambda: map(int, input())


def solve():
    s = input()
    s = s.lower()
    s = s.strip(".")
    A = [*s]
    ans = []
    for a in A:
        if "a" <= a <= "z" or "0" <= a <= "9" or a == "-" or a == "_" or a == ".":
            ans.append(a)

    ans2 = []
    cnt = 0
    for a in ans:
        if a == ".":
            cnt = 1
        else:
            if cnt:
                ans2.append(".")
            ans2.append(a)
            cnt = 0

    if not ans2:
        ans2 = ["a"]

    if len(ans2) <= 2:
        while len(ans2) != 3:
            ans2.append(ans2[-1])

    a = "".join(ans2[:15])
    a = a.strip(".")
    print(a)
    return


solve()
