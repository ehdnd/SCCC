import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(N, nums):
    isNo = False
    res = []
    can_push = [i for i in range(9, 0, -1)]
    stack = []
    for num in nums:
        while 1:
            if isNo:
                return "NO"

            if (not stack or stack[-1] < num) and can_push:
                stack.append(can_push.pop())
                res.append("+")
            elif stack[-1] == num:
                stack.pop()
                res.append("-")
                break
            else:
                isNo = True

    return res


N = int(input())
nums = [int(input()) for _ in range(N)]
res = jud(N, nums)
if res == "NO":
    print("NO")
else:
    for x in res:
        print(x)
