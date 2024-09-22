import sys

input = sys.stdin.readline
n = int(input())
cnt = 1

for i in range(n):
    cnt *= i + 1

print(cnt)
