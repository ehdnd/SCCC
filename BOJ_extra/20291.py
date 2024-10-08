import sys
from bisect import bisect_left, bisect_right

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

arr = []
for i in range(N):
    arr.append(input().split(".")[1])

arr.sort()
vs = sorted(list(set(arr)))

for x in vs:
    print(x, bisect_right(arr, x) - bisect_left(arr, x))
