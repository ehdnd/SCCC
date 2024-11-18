import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    # [수열 길이, 증가 감소 여부]
    # [증가중인 수열, 감소중인 수열]
    dp = [[1, 1] for _ in range(1000)]
    for i in range(N):
        for j in range(i):
            if nums[j] == nums[i]:
                continue

            # 증가중
            if dp[i][0]:
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][0] + 1)
                else:
                    # dp[i][0] = 0
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)

            # 감소중
            if dp[i][1]:
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][1] + 1)

    return max(dp, key=lambda x: x[1])[1]


# def jud():
#     # [수열 길이, 증가 감소 여부]
#     dp = [[1, 0] for _ in range(1000)]
#     for i in range(N):
#         for j in range(i):
#             if nums[i] == nums[j]:
#                 continue

#             # 0 이거나 증가중
#             if dp[j][1] >= 0:
#                 dp[i][0] = max(dp[i][0], dp[j][0] + 1)
#                 dp[i][1] = 1 if nums[j] < nums[i] else -1

#             # 0 이거나 감소중
#             if dp[i][1] <= 0 and nums[j] > nums[i]:
#                 dp[i][0] = max(dp[i][0], dp[j][0] + 1)
#                 dp[i][1] = -1

#     print(dp[:N])
#     res = 0
#     for a in dp:
#         if a[1] <= 0:
#             res = max(res, a[0])

#     return res


N = int(input())
nums = list(map(int, input().split()))
print(jud())
