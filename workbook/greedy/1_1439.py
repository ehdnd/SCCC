import sys

input = lambda: sys.stdin.readline().rstrip()
arr = input()
zero = 0
one = 0
pre = arr[0]
for i in range(1, len(arr)):
    if arr[i] == pre:
        continue
    else:
        if arr[i - 1] == "0":
            zero += 1
        else:
            one += 1
        pre = arr[i]

if arr[-1] == "0":
    zero += 1
else:
    one += 1

print(min(zero, one))
