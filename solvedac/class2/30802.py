import sys
import math

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

t_cnt = 0
for size in sizes:
    if size > 0:
        t_cnt += math.ceil(size / T)

p_cnt = N // P
p_extra = N % P

print(t_cnt)
print(p_cnt, p_extra)

# 왜틀림..?
# import sys

# input = lambda: sys.stdin.readline().rstrip()

# N = int(input())
# sizes = list(map(int, input().split()))
# T, P = map(int, input().split())

# t_cnt = 0
# for size in sizes:
#     if size > T:
#         if size % T != 0:
#             t_cnt += (t_cnt//T) + 1
#         else:
#             t_cnt += t_cnt // T
#     elif size > 0:
#         t_cnt += 1

# p_cnt = N // P
# p_extra = N % P

# print(t_cnt)
# print(p_cnt, p_extra)
