# 시간초과
# import sys

# input = lambda: sys.stdin.readline().rstrip()

# a, b, c = map(int, input().split())
# arr = []

# for i in range(1, b + 1):
#     res = a**i % c
#     if res not in arr:
#         arr.append(res)
#     else:
#         break

# print(arr[c % len(arr) + 1])