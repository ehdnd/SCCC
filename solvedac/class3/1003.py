import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

F = [[0, 0] for i in range(41)]
F[0] = [1, 0]
F[1] = [0, 1]

for i in range(2, 41):
    F[i][0] = F[i - 1][0] + F[i - 2][0]
    F[i][1] = F[i - 1][1] + F[i - 2][1]

for i in range(N):
    num = int(input())
    print(F[num][0], F[num][1])
