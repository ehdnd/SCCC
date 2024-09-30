import sys

input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())
limits = []
for _ in range(N):
    limits.append(int(input()))
limits.sort()

lack = sum(limits) - M

res = []
for i in range(N):
    evenly_give = lack // (N - i)
    limit = limits[i]
    if evenly_give <= limit:
        to_give = evenly_give
    else:
        to_give = limit

    lack -= to_give
    res.append(to_give)

cnt = 0
for x in res:
    cnt += x**2
print(cnt % 2**64)
