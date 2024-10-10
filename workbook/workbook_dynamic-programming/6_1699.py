import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

F = [0] * (N + 1)

for i in range(1, N + 1):
    if (i ** (1 / 2)).is_integer():
        F[i] = 0
