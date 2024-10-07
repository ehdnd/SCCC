import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ropes = [0] * N
for i in range(N):
    ropes[i] = int(input())

ropes.sort(reverse=True)

max = 0
for i in range(N - 1):
    max_1 = ropes[i] * (i + 1)
    max_2 = ropes[i + 1] * (i + 1 + 1)
    if max_1 > max_2:
        max = max_1
        break

if max == 0:
    max = ropes[-1] * N

print(max)
