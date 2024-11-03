import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


N = int(input())
M = int(input())
arr = list(map(lambda x: format(int(x), "b").zfill(20), input().split()))
print(arr)
