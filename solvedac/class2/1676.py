import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

res = 1
for i in range(1, N + 1):
    res *= i

res = list(str(res))
res.reverse()
cnt = 0
for char in res:
    if char == "0":
        cnt += 1
    else:
        break

print(cnt)
