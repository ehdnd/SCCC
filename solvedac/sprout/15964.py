import sys

input = lambda: sys.stdin.readline().rstrip()


def f(A, B):
    print((A + B) * (A - B))


a, b = map(int, input().split())
f(a, b)
