import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp = [0] * 1010
    for i in range(N):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1
    return max(dp)


N = int(input())
nums = list(map(int, input().split()))
print(jud())
