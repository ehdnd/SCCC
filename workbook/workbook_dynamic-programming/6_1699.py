import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
F = [0] * (N + 1)

for i in range(1, N + 1):
    if (i ** (1 / 2)).is_integer():
        F[i] = 1
        sq = i
    else:
        mini = 1000001
        for j in range(1, sq + 1):
            temp = F[j] + F[i - j]
            if temp < mini:
                mini = temp

        F[i] = min(F[i - 1] + 1, mini)

print(F[N])
