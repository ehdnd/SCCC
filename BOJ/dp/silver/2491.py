import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    dp1 = [1] * N
    for i in range(1, N):
        if nums[i - 1] <= nums[i]:
            dp1[i] = dp1[i - 1] + 1
    res1 = max(dp1)

    dp2 = [1] * N
    for i in range(1, N):
        if nums[i - 1] >= nums[i]:
            dp2[i] = dp2[i - 1] + 1
    res2 = max(dp2)

    return max(res1, res2)


N = int(input())
nums = list(map(int, input().split()))
print(jud())
