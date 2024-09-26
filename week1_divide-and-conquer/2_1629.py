import sys

input = lambda: sys.stdin.readline().rstrip()
a, b, c = map(int, input().split())

res = a
for _ in range(b):
    res *= a
    res %= c
print(res)
