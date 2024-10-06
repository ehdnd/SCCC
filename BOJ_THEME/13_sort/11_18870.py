import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
nums = list(map(int, input().split()))
arr = sorted(list(set(nums)))

dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i

for num in nums:
    print(dic[num], end=" ")
