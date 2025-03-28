# 모듈러 연산의 성질
import sys

input = lambda: sys.stdin.readline().rstrip()
A, B, C = map(int, input().split())


def jud(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (jud(A, B // 2, C) ** 2) % C
    else:
        return (jud(A, B // 2, C) ** 2) * A % C


print(jud(A, B, C))


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

# 시간초과2
# import sys

# input = lambda: sys.stdin.readline().rstrip()
# a, b, c = map(int, input().split())

# res = a
# for _ in range(b):
#     res *= a
#     res %= c
# print(res)
