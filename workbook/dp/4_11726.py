import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

F = [0] * 1001
F[1] = 1
F[2] = 2

for n in range(3, N + 1):
    F[n] = F[n - 2] + F[n - 1]
    F[n] %= 10007

print(F[N])
