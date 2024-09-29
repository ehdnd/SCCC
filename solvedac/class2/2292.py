import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

cnt = 1
i = 1
while 1:
    if N <= cnt:
        break
    cnt += 6 * i
    i += 1

print(i)
