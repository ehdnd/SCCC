import sys

input = lambda: sys.stdin.readline().rstrip()


def f(a, b):
    while 1:
        if b == 0:
            return a
        temp = a % b
        a = b
        b = temp


a, b = map(int, input().split())
r1 = f(a, b)
r2 = (a * b) // r1
print(r1)
print(r2)
