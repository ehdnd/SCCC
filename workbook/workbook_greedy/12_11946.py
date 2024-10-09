import sys

input = lambda: sys.stdin.readline().rstrip()


def jud(cases):
    cases.sort(key=lambda x: x[0])

    cnt = 0
    max = len(cases)
    for case in cases:
        if case[1] <= max:
            cnt += 1
            max = case[1]

    return cnt


N = int(input())
for i in range(N):
    n = int(input())
    cases = []
    for j in range(n):
        cases.append(list(map(int, input().split())))
    print(jud(cases))
