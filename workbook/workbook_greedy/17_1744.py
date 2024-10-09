import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())


def jud(nums):
    res = 0
    count = len(nums)
    if count < 2:
        res = sum(nums)
    else:
        for i in range(1, count, 2):
            res += nums[i - 1] * nums[i]
        if count % 2 != 0:
            res += nums[-1]
    return res


res = 0
minus_nums = []
plus_nums = []

for i in range(N):
    num = int(input())
    if num == 1:
        res += 1
    elif num > 0:
        plus_nums.append(num)
    else:
        minus_nums.append(num)

minus_nums.sort()
plus_nums.sort(reverse=True)

res += jud(minus_nums)
res += jud(plus_nums)

# if plus_count < 2:
#     res += sum(plus_nums)
# else:
#     for i in range(1, plus_count, 2):
#         res += plus_nums[i - 1] * plus_nums[i]
#     if plus_count % 2 != 0:
#         res += plus_nums[-1]

print(res)
