# if '666' in str(nth) 로 간단하게..

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())


def find6(list):
    cnt = 0
    for i in range(len(list)):
        if cnt >= 3:
            return True
        elif list[i] == "6":
            cnt += 1
        else:
            cnt = 0
    if cnt >= 3:
        return True
    return False


# 그냥 6이 세 개 이상만
# 6의 개수가 3개 이상이 되면 cnt 올려서 N에 도달하면 리턴하자
# 666부터 시작해서 1씩 증가시키자그냥
cnt = 1
res = 666

while 1:
    if cnt == N:
        break
    res += 1
    if find6(list(str(res))):
        cnt += 1

print(res)
