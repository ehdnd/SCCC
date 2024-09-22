# total .. cnt = 0 놓고 cnt += N
# 그냥 while 루프 쓰자

import sys


def total(lans, mid):
    temp = []
    for lan in lans:
        temp.append(lan // mid)
    total_made_lans = sum(temp)
    return total_made_lans


def search(lans, L, R, need):
    # 아직 탐색중
    if L <= R:
        mid = L + (R - L) // 2
        total_made_lans = total(lans, mid)

        if total_made_lans >= need:
            plus_one = total(lans, mid + 1)
            if plus_one < need:
                return mid
            else:
                L = mid + 1
                return search(lans, L, R, need)
        else:
            R = mid - 1
            return search(lans, L, R, need)

    else:
        return -1


input = sys.stdin.readline

K, need = map(int, input().strip().split())
lans = []
for i in range(K):
    lans.append(int(input()))

R = max(lans)
L = 1

print(search(lans, L, R, need))
