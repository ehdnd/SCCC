# 람다.. len(x) 사용필요
import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(input().strip())
li = list(set(li))

li.sort(key=lambda x: (len(x), x))

for i in li:
    print(i)
