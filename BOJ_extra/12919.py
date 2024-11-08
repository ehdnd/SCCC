import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def find(s, t):
    if s == t:
        return 1
    if len(s) >= len(t):
        return 0

    if t[-1] == "A" and find(s, t[:-1]):
        return 1
    if t[0] == "B" and find(s, t[:0:-1]):
        return 1

    return 0


S = input()
T = input()
print(find(S, T))
