import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())


def jud(case):
    res = 0
    for s in case:
        if s == "(":
            res += 1
        else:
            res -= 1
        if res < 0:
            return "NO"
    if res == 0:
        return "YES"
    else:
        return "NO"


for _ in range(N):
    case = input()
    print(jud(case))
