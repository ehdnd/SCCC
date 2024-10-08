import sys

input = lambda: sys.stdin.readline().rstrip()
arr = input()

isMinus = False
res = 0
temp = []

for char in arr:

    if char.isdigit():
        temp.append(char)
    else:
        temp = "".join(temp)
        num = int(temp)
        temp = []

        if isMinus:
            res -= num
        else:
            res += num

    if char == "-":
        isMinus = True

temp = "".join(temp)
num = int(temp)
temp = []
if isMinus:
    res -= num
else:
    res += num

print(res)
