# f1_시간초과) if target in targets 에서 50만 * 50만..

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
num = int(input())
targets = list(map(int, input().strip().split()))

arr.sort()

for target in targets:
    l_idx = bisect_left(arr, target, lo=0, hi=len(arr))
    if l_idx != len(arr) and arr[l_idx] == target:
        r_idx = bisect_right(arr, target)
        print(r_idx - l_idx, end=" ")

    else:
        print(0, end=" ")
