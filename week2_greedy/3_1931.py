# 종료시간이 먼저인 놈들을 먼저 배정한다고 해서 손해는 없다는 발상
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))

res = []
for meeting in meetings:
    if len(res) > 0:
        if res[-1][1] <= meeting[0]:
            res.append(meeting)
    else:
        res.append(meeting)

print(len(res))

# # fail1 - 잘못된 알고리즘
# import sys

# input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# meetings = []

# for _ in range(n):
#     meetings.append(list(map(int, input().split())))

# meetings.sort(reverse=True, key=lambda x: x[1] / (x[1] - x[0]))

# arr = []

# for meeting in meetings:
#     if len(arr) > 0:
#         if meeting[1] <= arr[-1][0]:
#             arr.append(meeting)
#     else:
#         arr.append(meeting)

# print(len(arr))

# #######################

# fail2 - (1,4), (2,4), (3,4) 면 어쩔건데.. x[1] 이 같으면 x[0] 으로 정렬
# import sys

# input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# meetings = []

# for _ in range(n):
#     meetings.append(list(map(int, input().split())))

# meetings.sort(key=lambda x: x[1])

# res = []
# for meeting in meetings:
#     if len(res) > 0:
#         if res[-1][1] <= meeting[0]:
#             res.append(meeting)
#     else:
#         res.append(meeting)

# print(len(res))
