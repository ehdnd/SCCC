import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    # [증가하는 수열 길이, 감소하는 수열 길이]
    dp = [[1, 1] for _ in range(1000)]
    for i in range(N):
        for j in range(i):
            if nums[j] == nums[i]:
                continue

            # 증가중
            if dp[i][0]:
                # 계속 증가
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][0] + 1)
                # 이제 감소
                else:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)

            # 감소중
            if dp[i][1] and nums[j] > nums[i]:
                # 계속 감소해야지
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
    # [5, 4, 3, 2, 1] 도 바이토닉 수열
    return max(map(max, dp))


N = int(input())
nums = list(map(int, input().split()))
print(jud())
