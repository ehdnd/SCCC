import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ropes = [0] * N
for i in range(N):
    ropes[i] = int(input())

ropes.sort(reverse=True)

res = []
for i in range(N):
    w_max = ropes[i] * (i + 1)
    res.append(w_max)

print(max(res))
