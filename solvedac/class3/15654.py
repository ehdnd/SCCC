import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(res):
    if len(res) == M:
        print(*res)
        return

    for num in nums:
        if num in res:
            continue
        res.append(num)
        jud(res)
        res.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
res = []
jud(res)
