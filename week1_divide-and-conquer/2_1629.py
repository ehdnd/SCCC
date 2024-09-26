import sys

input = lambda: sys.stdin.readline().rstrip()
a, b, c = map(int, input().split())

res = 0
for i in range(1, b + 1):
    res += a**i
    res %= c
print(res)
