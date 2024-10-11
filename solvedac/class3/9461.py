import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
F = [1] * 101
F[4] = 2
F[5] = 2
F[6] = 3
F[7] = 4
F[8] = 5

for i in range(8, 101):
    F[i] = F[i - 1] + F[i - 5]

for _ in range(N):
    print(F[int(input())])
