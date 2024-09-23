import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
temp = []

for i in range(n):
    temp.append(list(map(int, input().split())))

for arr in temp:
    H, W, N = arr

    X = N // H + 1
    Y = N % H

    if Y == 0:
        Y = H
        X -= 1

    print(str(Y) + str(X).rjust(2, "0"))
