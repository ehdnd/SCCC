import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(n):
    n = list(n)
    rev_n = list(reversed(n))
    if n == rev_n:
        return "yes"
    else:
        return "no"


while 1:
    n = input()
    if n == "0":
        break
    print(jud(n))
