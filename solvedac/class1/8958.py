# 굳이 cases 만들 필요 없이.. 바로바로 출력하자

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
cases = []
for _ in range(n):
    cases.append(input())

for case in cases:
    cnt = 0
    score = 0
    for ox in case:
        if ox == "O":
            cnt += 1
        else:
            cnt = 0
        score += cnt
    print(score)
