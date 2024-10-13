import sys

input = lambda: sys.stdin.readline().rstrip()


def jud():
    N = int(input())
    dic = {}
    for _ in range(N):
        item, kind = input().split()
        if kind in dic.keys():
            dic[kind] += 1
        else:
            dic[kind] = 1
    res = 1
    for n in dic.values():
        res *= n + 1
    return res - 1


N = int(input())
for _ in range(N):
    print(jud())
