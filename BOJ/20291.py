import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

dic = {}
for i in range(N):
    extension = input().split(".")[1]
    if not extension in dic:
        dic[extension] = 1
    else:
        dic[extension] += 1

sorted_dic = dict(sorted(dic.items()))

for key, value in sorted_dic.items():
    print(key, value)
