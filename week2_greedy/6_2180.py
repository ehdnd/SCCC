# import sys

# input = lambda: sys.stdin.readline().rstrip()

# N = int(input())
# fires = []
# etc = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     if b == 0:
#         continue
#     elif a == 0:
#         etc.append(b)
#     else:
#         fires.append([a, b])


# fires.sort(reverse=True, key=lambda x: (x[0] / x[1], x[0]))

# cnt = 0
# for fire in fires:
#     cnt += fire[0] * cnt + fire[1]
# cnt += sum(etc)
# print(cnt % 40000)

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
fires = []
for _ in range(N):
    a, b = map(int, input().split())
    if b == 0:
        continue
    else:
        fires.append([a, b])


fires.sort(reverse=True, key=lambda x: (x[0] / x[1], x[0]))

cnt = 0
for fire in fires:
    cnt += fire[0] * cnt + fire[1]
    cnt %= 40000
print(cnt)
