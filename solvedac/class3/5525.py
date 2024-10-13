import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
M = int(input())
P = input()

temp = 0
cnt = 0

start = 0
end = 3
while 1:
    if end > M:
        break

    if P[start:end] == "IOI":
        temp += 1
        start = end - 1
        end += 2

        if temp == N:
            cnt += 1
            temp -= 1
    else:
        start += 1
        end += 1
        temp = 0

print(cnt)
