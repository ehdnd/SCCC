import sys

input = lambda: sys.stdin.readline().rstrip()
arr = input()

minus_split_list = arr.split("-")

res = []
for x in minus_split_list:
    temp = list(map(int, x.split("+")))
    res.append(sum(temp))

num = res[0]
for i in range(1, len(res)):
    num -= res[i]

print(num)
