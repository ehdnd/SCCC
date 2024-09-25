import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

valid = False
for i in range(1, N + 1):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == N:
        valid = True
        break

if valid:
    print(i)
else:
    print(0)
