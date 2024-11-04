import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(nums, arr):
    print(round(sum(nums) / N))
    print(nums[N // 2])

    max = 0
    res = []
    for i in range(8001):
        if arr[i] > max:
            max = arr[i]
            res = [i - 4000]
        elif arr[i] == max:
            res.append(i - 4000)
    if len(res) > 1:
        print(res[1])
    else:
        print(res[0])

    print(abs(nums[-1] - nums[0]))


N = int(input())
arr = [0] * 8001
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
    arr[num + 4000] += 1
nums.sort()
jud(nums, arr)
