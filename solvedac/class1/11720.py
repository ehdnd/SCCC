import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = input()

cnt = 0
for i in a:
    cnt += int(i)

print(cnt)
