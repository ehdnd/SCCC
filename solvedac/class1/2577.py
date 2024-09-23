# [list].count(num) 으로 리스트 내 개수 반환 가능
# 세 줄 입력은 각각 따로 받을 수 있더라

import sys

input = lambda: sys.stdin.readline().rstrip()

nums = []
for i in range(3):
    nums.append(int(input()))

cnt = 1
for num in nums:
    cnt *= num

str = str(cnt)

cnt_arr = [0] * 10
for x in str:
    cnt_arr[int(x)] += 1

for i in range(10):
    print(cnt_arr[i])
