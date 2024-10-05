import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

F = [0] * (N + 1)

square = []
for i in range(1, N + 1):
    if i**2 > N:
        break
    F[i**2] = 1
    square.append(i**2)

for i in range(1, N + 1):
    if F[i] == 1:
        continue
    idx = 0
    for j in range(len(square)):
        if square[j] < i:
            idx = j
        else:
            break
    F[i] = F[i - square[idx]] + 1

print(F[N])
