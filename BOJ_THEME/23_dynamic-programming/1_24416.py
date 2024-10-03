# 아니 15회 아님..? 왜 이게 5번인지 모르겠네
import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

F = [0] * (N + 1)
F[0] = 0
if N != 0:
    F[1] = 1
for i in range(2, N + 1):
    F[i] = F[i - 2] + F[i - 1]

print(F[N], end=" ")
print(N - 2)
# def fib(n):
#     global cnt

#     if n == 1 or n == 2:
#         return 1
#     else:
#         cnt += 1
#         return fib(n - 1) + fib(n - 2)


# cnt = 0
# fib(N)
# print(cnt)
