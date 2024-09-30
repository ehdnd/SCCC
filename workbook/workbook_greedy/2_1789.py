import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

num = 0
cnt = 0
for i in range(1, N):
    if num > N:
        cnt -= 1
        break
    elif num == N:
        break
    num += i
    cnt += 1
print(cnt)
