import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
N %= 1500000
C = 1000000
F = [0] * (N + 1)
F[1] = 1

for i in range(2, N + 1):
    F[i] = ((F[i - 1] % C) + (F[i - 2] % C)) % C
    # if F[i] == 1 and F[i-1] == 0:
    #     print(i-1)
    #     break
print(F[N])
