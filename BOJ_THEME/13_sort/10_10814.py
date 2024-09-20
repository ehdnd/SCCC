# 데이터 어떻게 입력받냐,,
# 그냥 a, b = input().strip().split() 으로 가자
import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    a, b = map(str, input().strip().split())
    li.append([int(a), b])

li.sort(key=lambda x: x[0])

for i in li:
    print(i[0], i[1])
