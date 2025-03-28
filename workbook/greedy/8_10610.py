# 3의 배수 조건: 각 자리 수의 합이 3의 배수
import sys

input = lambda: sys.stdin.readline().rstrip()
N = input()
arr = sorted(list(N), reverse=True)
cnt = 0
for x in N:
    cnt += int(x)
if arr[-1] == "0" and cnt % 3 == 0:
    for char in arr:
        print(char, end="")
else:
    print(-1)
