import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
cases = []
for _ in range(N):
    cases.append(list(map(int, input().split())))

cases.sort(key=lambda x: (x[0], x[1]))

cnt = 0
temp = cases
while 1:
    if temp == []:
        break

    cases = temp
    temp = []
    res = []
    for case in cases:
        if len(res) > 0:
            if res[-1][1] <= case[0]:
                res.append(case)
            else:
                temp.append(case)
        else:
            res.append(case)
    cnt += 1

print(cnt)
