import sys

sys.setrecursionlimit(10**9)

input = lambda: sys.stdin.readline().rstrip()


def find(s, t):
    if s == t:
        return 1
    if len(s) >= len(t):
        return 0

    res1, res2 = 0, 0
    if t[0] == "B":
        t1 = t[1:][::-1]
        res1 = find(s, t1)
    if t[-1] == "A":
        t2 = t[:-1]
        res2 = find(s, t2)

    return max(res1, res2)


S = input()
T = input()
print(find(S, T))
