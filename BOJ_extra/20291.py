import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

arr = []
for i in range(N):
    arr.append(input().split(".")[1])

vs = sorted(list(set(arr)))

for x in vs:
    print(x, arr.count(x))
